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

    for i in range(30):
        temp = random.uniform(plant[1], plant[2])
        humidity = random.uniform(plant[3], plant[4])
        light = random.uniform(plant[5], plant[6])
        score = random.uniform(80, 100)
        X.append([plantIndex, temp, humidity, light])
        y.append(score)

    for i in range(20):
        temp = random.uniform(plant[1] - 15, plant[2] + 15)
        humidity = random.uniform(plant[3] - 15, plant[4] + 15)
        light = random.uniform(plant[5] * 0.5, plant[6] * 1.5)
        score = random.uniform(40, 70)
        X.append([plantIndex, temp, humidity, light])
        y.append(score)

    for i in range(20):
        temp = random.uniform(plant[1] - 30, plant[2] + 30)
        humidity = random.uniform(0, 100)
        light = random.uniform(0, 30000)
        score = random.uniform(0, 30)
        X.append([plantIndex, temp, humidity, light])
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