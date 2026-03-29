import board
import time
import digitalio
import analogio
import adafruit_dht
import adafruit_character_lcd.character_lcd as character_lcd
from model import predict # removed in 'combined.py' as 'model.py' and 'code.py' are combined together.

photocell = analogio.AnalogIn(board.A0)
dht_device = adafruit_dht.DHT11(board.D5)

btn_up = digitalio.DigitalInOut(board.A1)
btn_up.direction = digitalio.Direction.INPUT
btn_up.pull = digitalio.Pull.UP

btn_down = digitalio.DigitalInOut(board.A2)
btn_down.direction = digitalio.Direction.INPUT
btn_down.pull = digitalio.Pull.UP

btn_select = digitalio.DigitalInOut(board.A3)
btn_select.direction = digitalio.Direction.INPUT
btn_select.pull = digitalio.Pull.UP

led_red = digitalio.DigitalInOut(board.A4)
led_red.direction = digitalio.Direction.OUTPUT
led_green = digitalio.DigitalInOut(board.A5)
led_green.direction = digitalio.Direction.OUTPUT
led_blue = digitalio.DigitalInOut(board.SCK)
led_blue.direction = digitalio.Direction.OUTPUT


def get(): #returns temp, humidity, light
    temperature_c = dht_device.temperature
    humidity = dht_device.humidity
    light = photocell.value * (18000 / 65535)
    # Convert to Fahrenheit
    temperature_f = temperature_c * (9 / 5) + 32
    return temperature_f,humidity,light


#hardware:https://docs.circuitpython.org/projects/charlcd/en/latest/
#LCD

# LCD Setup
lcd_rs = digitalio.DigitalInOut(board.D13)
lcd_en = digitalio.DigitalInOut(board.D12)
lcd_d4 = digitalio.DigitalInOut(board.D11)
lcd_d5 = digitalio.DigitalInOut(board.D10)
lcd_d6 = digitalio.DigitalInOut(board.D9)
lcd_d7 = digitalio.DigitalInOut(board.D6)
lcd_columns = 16
lcd_rows = 2
lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

def set_led(r, g, b):
    led_red.value = r
    led_green.value = g
    led_blue.value = b

plantDict = {
    0: "Aeonium",
    1: "African Mask Plant",
    2: "African Violet",
    3: "Agave",
    4: "Aglaonema Silver Bay",
    5: "Air Plant",
    6: "Aloe Vera",
    7: "Aluminum Plant",
    8: "Amaryllis",
    9: "Angel Wing Begonia",
    10: "Anthurium",
    11: "Areca Palm",
    12: "Arrowhead Plant",
    13: "Asparagus Fern",
    14: "Aster",
    15: "Baby Rubber Plant",
    16: "Baby Tears",
    17: "Bamboo Palm",
    18: "Banana Plant",
    19: "Basil",
    20: "Bay Laurel",
    21: "Bird of Paradise",
    22: "Birds Nest Fern",
    23: "Black Eyed Susan Vine",
    24: "Bleeding Heart Vine",
    25: "Blood Leaf",
    26: "Blue Star Fern",
    27: "Bonsai Ficus",
    28: "Boston Fern",
    29: "Bougainvillea",
    30: "Boxwood",
    31: "Bromeliad",
    32: "Bunny Ear Cactus",
    33: "Burros Tail",
    34: "Button Fern",
    35: "Cactus",
    36: "Caladium",
    37: "Calathea",
    38: "Cape Primrose",
    39: "Cardinal Flower",
    40: "Carnation",
    41: "Cast Iron Plant",
    42: "Chain of Hearts",
    43: "Chamomile",
    44: "Chinese Evergreen",
    45: "Chinese Money Plant",
    46: "Christmas Cactus",
    47: "Chrysanthemum",
    48: "Cilantro",
    49: "Cineraria",
    50: "Citronella",
    51: "Clematis",
    52: "Coffee Plant",
    53: "Coleus",
    54: "Coral Bells",
    55: "Corn Plant",
    56: "Creeping Fig",
    57: "Croton",
    58: "Crown of Thorns",
    59: "Cyclamen",
    60: "Daffodil",
    61: "Dahlia",
    62: "Desert Rose",
    63: "Dieffenbachia",
    64: "Dill",
    65: "Donkey Tail",
    66: "Dracaena",
    67: "Dracaena Marginata",
    68: "Dragon Tree",
    69: "Dumb Cane",
    70: "Dwarf Banana",
    71: "Dwarf Citrus",
    72: "Dwarf Umbrella Tree",
    73: "Easter Lily",
    74: "Echeveria",
    75: "Elephant Ear",
    76: "English Ivy",
    77: "Eucalyptus",
    78: "False Aralia",
    79: "Fatsia Japonica",
    80: "Fern Leaf Cactus",
    81: "Fiddle Leaf Fig",
    82: "Firecracker Plant",
    83: "Fittonia",
    84: "Flaming Katy",
    85: "Flamingo Flower",
    86: "Foxglove",
    87: "Frangipani",
    88: "Friendship Plant",
    89: "Fuchsia",
    90: "Gardenia",
    91: "Geranium",
    92: "Gerbera Daisy",
    93: "Globe Amaranth",
    94: "Goldfish Plant",
    95: "Grape Ivy",
    96: "Haworthia",
    97: "Heartleaf Philodendron",
    98: "Heliotrope",
    99: "Hens and Chicks",
    100: "Hibiscus",
    101: "Hindu Rope Plant",
    102: "Hoya",
    103: "Hyacinth",
    104: "Hydrangea",
    105: "Impatiens",
    106: "Inch Plant",
    107: "Jade Plant",
    108: "Janet Craig Dracaena",
    109: "Japanese Maple Bonsai",
    110: "Jasmine",
    111: "Kangaroo Paw Fern",
    112: "Kentia Palm",
    113: "Kumquat",
    114: "Lace Aloe",
    115: "Lantana",
    116: "Lavender",
    117: "Lemon Balm",
    118: "Lemon Button Fern",
    119: "Lipstick Plant",
    120: "Lithops",
    121: "Lucky Bamboo",
    122: "Madagascar Dragon Tree",
    123: "Maidenhair Fern",
    124: "Majesty Palm",
    125: "Mandevilla",
    126: "Maranta",
    127: "Marigold",
    128: "Meyer Lemon",
    129: "Mint",
    130: "Money Tree",
    131: "Monstera",
    132: "Moses in the Cradle",
    133: "Nerve Plant",
    134: "Norfolk Island Pine",
    135: "Oleander",
    136: "Orchid",
    137: "Oregano",
    138: "Oxalis",
    139: "Pachira",
    140: "Painted Lady Philodendron",
    141: "Panda Plant",
    142: "Pansy",
    143: "Paperwhite Narcissus",
    144: "Parlor Palm",
    145: "Parsley",
    146: "Passion Flower",
    147: "Peace Lily",
    148: "Peacock Plant",
    149: "Peperomia",
    150: "Periwinkle",
    151: "Petunia",
    152: "Philodendron",
    153: "Piggyback Plant",
    154: "Pilea",
    155: "Pink Quill",
    156: "Pitcher Plant",
    157: "Polka Dot Plant",
    158: "Ponytail Palm",
    159: "Pothos",
    160: "Prayer Plant",
    161: "Primrose",
    162: "Purple Passion Plant",
    163: "Purple Waffle Plant",
    164: "Rabbit Foot Fern",
    165: "Ranunculus",
    166: "Rattlesnake Plant",
    167: "Rex Begonia",
    168: "Rosemary",
    169: "Rubber Plant",
    170: "Sage",
    171: "Sago Palm",
    172: "Satin Pothos",
    173: "Schefflera",
    174: "Sensitive Plant",
    175: "Shamrock Plant",
    176: "Shrimp Plant",
    177: "Silver Satin Pothos",
    178: "Snake Plant",
    179: "Snapdragon",
    180: "Spider Plant",
    181: "Staghorn Fern",
    182: "String of Bananas",
    183: "String of Pearls",
    184: "Stromanthe",
    185: "Succulent",
    186: "Swedish Ivy",
    187: "Sweet Potato Vine",
    188: "Swiss Cheese Plant",
    189: "Thyme",
    190: "Ti Plant",
    191: "Tulip",
    192: "Umbrella Plant",
    193: "Venus Fly Trap",
    194: "Wandering Jew",
    195: "Wax Plant",
    196: "Weeping Fig",
    197: "Yucca",
    198: "Zebra Plant",
    199: "Zinnia",
    200: "ZZ Plant"
}

i = 0
last_read = 0
temp, humidity, light = 0, 0, 0
last_message = ""

lcd.message = "PlantWise\nLoading..."
while temp == 0:
    try:
        temp, humidity, light = get()
        light = photocell.value * (18000 / 65535)
    except (RuntimeError, OSError):
        time.sleep(2)

while True:
    # Check buttons
    if not btn_up.value:
        i = (i - 1) % len(plantDict)
        time.sleep(0.2)
    if not btn_down.value:
        i = (i + 1) % len(plantDict)
        time.sleep(0.2)

    # Read sensors every 2 seconds
    current_time = time.monotonic()
    if current_time - last_read > 2:
        try:
            temp, humidity, light = get()

            print(f"T: {temp} H: {humidity} L: {light} Plant: {i}")
        except (RuntimeError, OSError):
            pass
        last_read = current_time

    # Predict and display
    predictionNum = predict(i, temp, humidity, light)
    message = plantDict[i] + "\n" + str(round(predictionNum)) + "% suitable"
    
    if message != last_message:
        lcd.clear()
        lcd.message = message
        last_message = message

    if predictionNum >= 75:
        set_led(False, True, False)  # green
    elif predictionNum >= 35:
        set_led(True, True, False)   # yellow
    else:
        set_led(True, False, False)  # red
    

    time.sleep(0.05)