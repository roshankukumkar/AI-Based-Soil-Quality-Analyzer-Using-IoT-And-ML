# AI-Based Soil Quality Analyzer Using IoT

An IoT and Machine Learning based system for monitoring soil and recommending suitable crops based on soil and environmental parameters.

## Project Overview

The **AI-Based Soil Quality Analyzer Using IoT** collects soil and environmental data using sensors connected to an ESP32/Arduino device.

The collected values are processed by a Flask-based Python application. A **Random Forest Classifier** is used to predict the most suitable crop based on the input parameters.

The system uses:

* Soil Moisture
* Temperature
* Humidity
* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* pH
* Rainfall

The predicted crop and confidence value are displayed through a web interface.

## System Flow

```text
Soil & Environmental Sensors
            ↓
       ESP32 / Arduino
            ↓
       Serial Communication
            ↓
       Flask Backend
            ↓
      Data Processing
            ↓
    Random Forest Model
            ↓
      Crop Prediction
            ↓
       Web Interface
```

## Technologies Used

### Backend

* Python
* Flask
* NumPy
* Pandas
* PySerial

### Machine Learning

* Scikit-learn
* Random Forest Classifier
* Label Encoding

### Frontend

* HTML
* CSS

### Hardware / IoT

* ESP32 / Arduino
* Soil Moisture Sensor
* DHT11
* NPK Sensor
* MAX485

## Project Structure

```text
IOT_AI-BASED-SQA/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── test_serial.py
│
├── dataset/
│   └── Crop_recommendation (1).csv
│
├── ml/
│   ├── crop_model.pkl
│   ├── label_encoder.pkl
│   ├── scaler.pkl
│   ├── crop_recommendation.py
│   └── train_and_save_model.py
│
├── static/
│   └── images/
│
└── templates/
    ├── analysis.html
    ├── index.html
    ├── recommendation.html
    └── result.html
```

## Machine Learning

The project uses a **Random Forest Classifier** for crop prediction.

The model uses the following features:

```text
N
P
K
temperature
humidity
soil_moisture
ph
rainfall
```

The model is trained using the crop recommendation dataset and the trained model is saved using Python Pickle.

## Flask Application

The Flask application:

1. Loads the trained machine learning model.
2. Loads the label encoder.
3. Reads sensor values through serial communication.
4. Receives N, P, K, pH and rainfall values from the web interface.
5. Combines these values with temperature, humidity and soil moisture.
6. Sends the values to the Random Forest model.
7. Predicts the suitable crop.
8. Calculates the prediction confidence.
9. Displays the result through the web interface.

## Dataset

The project contains a crop recommendation dataset in:

```text
dataset/Crop_recommendation (1).csv
```

The dataset contains soil and environmental parameters used for crop prediction.

## Running the Project

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

### 2. Open the project directory

```bash
cd IOT_AI-BASED-SQA
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python app.py
```

The application will run locally using Flask.

## Hardware

The original project uses an ESP32/Arduino-based setup for collecting sensor data.

The sensor data is transferred to the Python application through serial communication.

> Note: The hardware is not required to view the source code and understand the software/ML implementation. Actual sensor-based operation requires the corresponding hardware setup and serial connection.

## Results

The project report describes the developed system as a low-cost IoT and Machine Learning based crop recommendation system.

The report's results section reports **97% accuracy** for the Random Forest model.

## Future Scope

Possible future improvements include:

* Adding more sensors
* Improving real-time monitoring
* Expanding the crop dataset
* Deploying the application online
* Improving the prediction model
* Adding additional agricultural recommendations

## Author

**Roshan Kukumkar**

MCA Graduate
Central University of Karnataka

## Project Type

**IoT | Machine Learning | Flask | Python | Web Application**
