# PlantWise

**"It's PlantWise, otherwise it's none the wise."**

A handheld, AI-powered plant suitability checker built at Hardware Hack 2026 UF. PlantWise uses real-time environmental sensor data and a trained machine learning model to determine how well a plant will thrive in any given location — no laptop or phone required.

## How It Works

1. **Scroll** through 200+ houseplants using the physical buttons
2. **Place** the device in any location — a windowsill, desk, patio, etc.
3. **Read** the suitability score on the LCD screen (0–90%)
4. **Check** the RGB LED for instant feedback:
   - Green — great spot for this plant
   - Yellow — moderate conditions
   - Red — not suitable

## Hardware

- **Adafruit Feather ESP32-S3** (4MB Flash, 2MB PSRAM) — running CircuitPython
- **DHT11** — temperature and humidity sensor
- **Photoresistor** — ambient light level sensor
- **LCD1602** — 16x2 character display
- **RGB LED** — visual suitability indicator
- **3x Push Buttons** — scroll up, scroll down, select
- **Potentiometer** — LCD contrast control

## The AI

PlantWise uses a **Decision Tree Regressor** trained with scikit-learn on ~20,000 data points generated from real horticultural growing condition ranges for 200 houseplants. The trained model was exported as a pure Python function (if/else decision logic) so it runs directly on the microcontroller with **zero external dependencies**.

### Training Pipeline

1. Plant condition data (temperature, humidity, light ranges) compiled into `resources/plant_conditions.csv`
2. Training samples generated across the full range of conditions with suitability scores based on distance from each plant's ideal range
3. Decision Tree Regressor trained with `max_depth=10` using scikit-learn
4. Model exported as `model.py` — a standalone Python predict function
5. Model copied to ESP32-S3 and runs locally on-device

## Project Structure

```
PlantWise/
├── src/
│   ├── code.py              # Main program (runs on ESP32-S3)
│   ├── hardware.py           # Sensor and LCD setup/functions
│   └── model.py              # Exported ML model (auto-generated)
├── training/
│   └── trainingModel.py      # scikit-learn training script (runs on laptop)
├── lib/
│   ├── adafruit_character_lcd/   # CircuitPython LCD library
│   └── adafruit_dht.mpy         # CircuitPython DHT sensor library
├── resources/
│   └── plant_conditions.csv  # Plant growing condition dataset (200 plants)
├── firmware/
│   └── circuitPython_firmware.uf2  # CircuitPython firmware for ESP32-S3
├── arduino/
│   └── Arduino_IDEVersion_c.txt    # Original Arduino C version
├── combined.py               # All-in-one file deployed to ESP32-S3
├── LICENSE
└── README.md
```

## Replicating This Project

### What You Need

- Adafruit Feather ESP32-S3 (4MB Flash / 2MB PSRAM)
- DHT11 temperature & humidity sensor
- Photoresistor + 10K resistor
- LCD1602 (16x2 character LCD)
- RGB LED + 220Ω resistors
- 3x push buttons
- Breadboard and jumper wires
- USB-C data cable
- Potentiometer (for LCD contrast)

### Setup

1. **Flash CircuitPython** — Double-tap Reset on the ESP32-S3, drag `firmware/circuitPython_firmware.uf2` onto the FTHRS3BOOT drive
2. **Install libraries** — Copy the `lib/` folder contents to the CIRCUITPY drive's `lib/` folder
3. **Deploy code** — Copy `combined.py` to the CIRCUITPY drive as `code.py`
4. **Wire components** — See pin assignments below
5. **Power on** — The device will display "PlantWise Loading..." then start

### Pin Assignments (ESP32-S3 Feather)

| Component | Pin |
|-----------|-----|
| LCD RS | D13 |
| LCD EN | D12 |
| LCD D4 | D11 |
| LCD D5 | D10 |
| LCD D6 | D9 |
| LCD D7 | D6 |
| DHT11 Data | D5 |
| Photoresistor | A0 |
| Button Up | A1 |
| Button Down | A2 |
| Button Select | A3 |
| LED Red | A4 |
| LED Green | A5 |
| LED Blue | SCK |

### Retraining the Model

If you want to modify the plant dataset or retrain the model:

```bash
pip install scikit-learn numpy
python training/trainingModel.py
```

This generates a new `model.py` that can be deployed to the device.

## Built At

**Hardware Hack 2026** — University of Florida | March 28–29, 2026

## Team

- Javier Coll-Roman
- Sreesha Variseri
- Rahmatulloh Fakhriddin

## License

MIT License
