import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Load the dataset
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Preprocess the data
def preprocess_data(data):
    # Convert 'Time' column to float for easier numerical processing
    data['Time'] = data['Time'].astype(float)

    # Handle missing values (drop rows with missing values)
    data = data.dropna()

    # Encode 'Protocol' and 'Info' columns (optional)
    data['Protocol'] = data['Protocol'].astype('category').cat.codes
    data['Info'] = data['Info'].astype('category').cat.codes

    # Remove duplicates
    data = data.drop_duplicates()

    # Calculate time difference between consecutive packets
    data['Time_diff'] = data['Time'].diff().fillna(0)

    # Calculate rolling mean for packet length (e.g., last 5 packets)
    data['Length_mean'] = data['Length'].rolling(window=5).mean().fillna(0)

    return data

# Anomaly detection using Isolation Forest
def detect_anomalies(data):
    # Select features for anomaly detection
    features = data[['Time', 'Length', 'Time_diff', 'Protocol']]

    # Initialize the Isolation Forest model
    model = IsolationForest(contamination=0.05)
    model.fit(features)

    # Predict anomalies (-1 for anomaly, 1 for normal)
    data['Anomaly'] = model.predict(features)
    data['Anomaly'] = data['Anomaly'].apply(lambda x: 1 if x == -1 else 0)

    return data

# Function to visualize anomalies
def visualize_anomalies(data):
    # Plot the anomalies
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Time'], data['Length'], c=data['Anomaly'], cmap='coolwarm', label='Anomaly')
    plt.title('Network Traffic Anomaly Detection')
    plt.xlabel('Time')
    plt.ylabel('Packet Length')
    plt.legend()
    plt.show()

# Main function
def main():
    # Load the data
    file_path = '/content/Datafile.csv'  # Path to your dataset in Colab
    data = load_data(file_path)

    # Preprocess the data
    data = preprocess_data(data)

    # Detect anomalies
    data = detect_anomalies(data)

    # Visualize anomalies
    visualize_anomalies(data)

    # Display anomalies
    print(f"Detected anomalies:\n{data[data['Anomaly'] == 1]}")

if __name__ == "__main__":
    main()
