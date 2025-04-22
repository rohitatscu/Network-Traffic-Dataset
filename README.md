# Network-Traffic-Dataset

Project Overview
This project demonstrates the development of a Real-Time Anomaly Detection Pipeline designed to monitor and detect unusual patterns in network traffic data. The pipeline leverages machine learning algorithms and real-time streaming technologies to continuously process network traffic data, identifying and alerting on potential anomalies or security threats.

Technologies Used
Python: The primary programming language used to build the anomaly detection pipeline.

Scikit-learn: Utilized for Isolation Forest, an unsupervised anomaly detection model.

TensorFlow/Keras: Used for building an LSTM Autoencoder to detect more complex anomalies.

PySpark/Flink: For distributed stream processing, handling large datasets in real time.

Kafka: Simulating the streaming of network traffic data in real-time.

Docker: To containerize the application, ensuring portability and consistency across different environments.

Google Colab: Used for prototyping and running the anomaly detection models and experiments.

Dataset
The dataset used for anomaly detection is a Network Traffic Dataset containing various network traffic packets with features such as packet length, protocol, source, and destination IP addresses. The data is included in this repository as a ZIP file (Datafile.zip) due to its large size.

File: Datafile.zip
This file contains a CSV file with network traffic data, which can be extracted to work with the data in the anomaly detection pipeline.

To extract and use the data:

bash
Copy
unzip Datafile.zip
Anomaly Detection Process
1. Data Preprocessing:
The raw network traffic data is cleaned by handling missing values and encoding categorical columns such as Protocol and Info.

Features like Time difference between consecutive packets and rolling mean of packet length are computed.

2. Anomaly Detection:
Isolation Forest is applied to detect outliers in the dataset, labeling suspicious traffic as anomalies.

LSTM Autoencoder is an optional model that can be used to detect more complex anomalies based on time-series patterns in the data.

3. Real-Time Processing:
The pipeline simulates real-time processing using Kafka to ingest the data and detect anomalies in real time.

The trained models are deployed to process incoming streams of network data, alerting whenever an anomaly is detected.

4. Visualization:
The pipeline visualizes anomalies on a scatter plot, using packet time and length as the axes, where anomalies are color-coded for easy identification.

How to Run the Code
Clone this repository:

bash
Copy
git clone https://github.com/rohitatscu/Network-Traffic-Dataset.git
Install required dependencies:

bash
Copy
pip install -r requirements.txt
Extract the dataset:

If you haven't already extracted the dataset, you can unzip Datafile.zip:

bash
Copy
unzip Datafile.zip
Run the Python script:

To run the pipeline, execute the network_traffic.py script:

bash
Copy
python network_traffic.py
This will load the dataset, preprocess it, detect anomalies, and display the visualized results.Project Overview
This project demonstrates the development of a Real-Time Anomaly Detection Pipeline designed to monitor and detect unusual patterns in network traffic data. The pipeline leverages machine learning algorithms and real-time streaming technologies to continuously process network traffic data, identifying and alerting on potential anomalies or security threats.

Technologies Used
Python: The primary programming language used to build the anomaly detection pipeline.

Scikit-learn: Utilized for Isolation Forest, an unsupervised anomaly detection model.

TensorFlow/Keras: Used for building an LSTM Autoencoder to detect more complex anomalies.

PySpark/Flink: For distributed stream processing, handling large datasets in real time.

Kafka: Simulating the streaming of network traffic data in real-time.

Docker: To containerize the application, ensuring portability and consistency across different environments.

Google Colab: Used for prototyping and running the anomaly detection models and experiments.

Dataset
The dataset used for anomaly detection is a Network Traffic Dataset containing various network traffic packets with features such as packet length, protocol, source, and destination IP addresses. The data is included in this repository as a ZIP file (Datafile.zip) due to its large size.

File: Datafile.zip
This file contains a CSV file with network traffic data, which can be extracted to work with the data in the anomaly detection pipeline.

To extract and use the data:

bash
Copy
unzip Datafile.zip
Anomaly Detection Process
1. Data Preprocessing:
The raw network traffic data is cleaned by handling missing values and encoding categorical columns such as Protocol and Info.

Features like Time difference between consecutive packets and rolling mean of packet length are computed.

2. Anomaly Detection:
Isolation Forest is applied to detect outliers in the dataset, labeling suspicious traffic as anomalies.

LSTM Autoencoder is an optional model that can be used to detect more complex anomalies based on time-series patterns in the data.

3. Real-Time Processing:
The pipeline simulates real-time processing using Kafka to ingest the data and detect anomalies in real time.

The trained models are deployed to process incoming streams of network data, alerting whenever an anomaly is detected.

4. Visualization:
The pipeline visualizes anomalies on a scatter plot, using packet time and length as the axes, where anomalies are color-coded for easy identification.

How to Run the Code
Clone this repository:

bash
Copy
git clone https://github.com/rohitatscu/Network-Traffic-Dataset.git
Install required dependencies:

bash
Copy
pip install -r requirements.txt
Extract the dataset:

If you haven't already extracted the dataset, you can unzip Datafile.zip:

bash
Copy
unzip Datafile.zip
Run the Python script:

To run the pipeline, execute the network_traffic.py script:

bash
Copy
python network_traffic.py
This will load the dataset, preprocess it, detect anomalies, and display the visualized results.
