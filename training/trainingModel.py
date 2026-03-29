import csv
import random
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.tree import _tree
import numpy as np

plantDict = {}

with open('resources/plant_conditions.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    
    i = 0

    for row in reader:
        plantDict[i] = [row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6])]
        i += 1


X = []
y = []

for plantIndex in plantDict:

    plant = plantDict[plantIndex]

    for i in range(100):
    # Random conditions across full range
        temp = random.uniform(30, 110)
        humidity = random.uniform(0, 100)
        light_val = random.uniform(0, 30000)
        
        # Calculate how far outside ranges
        temp_off = max(0, plant[1] - temp, temp - plant[2])
        hum_off = max(0, plant[3] - humidity, humidity - plant[4])
        light_off = max(0, plant[5] - light_val, light_val - plant[6])
        
        # Gentler penalty curve
        score = max(0, min(90, 90 - (temp_off * 1) - (hum_off * 0.8) - (light_off * 0.003)))
        
        X.append([plantIndex, temp, humidity, light_val])
        y.append(score)


clf = DecisionTreeRegressor(max_depth=10)
clf.fit(X, y)

def tree_to_python(tree, feature_names):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined"
        for i in tree_.feature
    ]

    lines = []
    lines.append("def predict(plant, temp, humidity, light):")

    def recurse(node, depth):
        indent = "    " * (depth + 1)
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = round(tree_.threshold[node], 2)
            lines.append(f"{indent}if {name} <= {threshold}:")
            recurse(tree_.children_left[node], depth + 1)
            lines.append(f"{indent}else:")
            recurse(tree_.children_right[node], depth + 1)
        else:
            value = round(tree_.value[node][0][0], 2)
            lines.append(f"{indent}return {value}")

    recurse(0, 0)
    return "\n".join(lines)

python_code = tree_to_python(clf, ['plant', 'temp', 'humidity', 'light'])

with open('model.py', 'w') as f:
    f.write(python_code)

print("Model exported to model.py")