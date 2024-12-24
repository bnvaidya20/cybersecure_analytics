import pandas as pd
import yaml
import gzip

import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder, StandardScaler


def load_ad_data(data_path):
    with gzip.open(data_path, 'rt') as f_in:
        # Load YAML content
        yaml_data = yaml.safe_load(f_in)

    data = pd.DataFrame(yaml_data)
    return data

def encode_categorical_columns(data, categorical_cols):
    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        label_encoders[col] = le

def run_anomaly_detection(data, contamination=0.01):
    # Preprocess data
    timestamp_column = data['timestamp']

    categorical_cols = ['classification', 'protocol', 'source', 'destination']
    encode_categorical_columns(data, categorical_cols)

    # Normalize numerical columns
    scaler = StandardScaler()
    numerical_cols = ['sid', 'priority', 'port']
    data[numerical_cols] = scaler.fit_transform(data[numerical_cols])

    # Train Isolation Forest
    iso_forest = IsolationForest(n_estimators=100, contamination=contamination, random_state=42)
    iso_forest.fit(data[numerical_cols])
    data['anomaly'] = iso_forest.predict(data[numerical_cols])
    data['anomaly'] = data['anomaly'].map({1: 'Normal', -1: 'Anomaly'})

    anomalies_count = data['anomaly'].value_counts()
    anomalies = data[data['anomaly'] == 'Anomaly']

    return data, timestamp_column, anomalies_count, anomalies

# Categorize port ranges
def categorize_port(port):
    if port <= 1023:
        return 'Well-Known'
    elif port <= 49151:
        return 'Registered'
    else:
        return 'Dynamic'
    
def run_anomaly_detection_feature_eng(data, contamination=0.01):
    # Preprocess data
    timestamp_column = data['timestamp']

    categorical_cols = ['classification', 'protocol', 'source', 'destination']
    encode_categorical_columns(data, categorical_cols)

    # Create source-destination pair count
    data['src_dest_count'] = data.groupby(['source', 'destination'])['sid'].transform('count')

    # Create port ranges
    data['port_range'] = data['port'].apply(categorize_port)

    # Convert 'timestamp' to datetime format
    data['timestamp'] = pd.to_datetime(timestamp_column, errors='coerce')
    # Drop rows with invalid timestamps
    data.dropna(subset=['timestamp'], inplace=True)
    # Set 'timestamp' as index for time-based aggregation
    data.set_index('timestamp', inplace=True)

    # Check for duplicates in the timestamp index
    if data.index.duplicated().any():
        print("Duplicates found in the timestamp index. Resolving...")
        # Option A: Aggregate duplicates
        data = data.groupby(data.index).agg({
            'sid': 'count',  # Count events
            'classification': 'first',
            'priority': 'mean',
            'protocol': 'first',
            'source': 'first',
            'destination': 'first',
            'port': 'mean',
            'src_dest_count': 'sum',
            'port_range': 'first'
        })

    # Create the 'events_per_min' feature
    data['events_per_min'] = data.groupby(pd.Grouper(freq='1Min'))['sid'].transform('count')

    # Reset index if needed
    data.reset_index(inplace=True)

    # Drop non-informative columns
    data.drop(columns=['timestamp'], inplace=True)

    # Encode categorical columns
    categorical_cols = ['port_range']
    encode_categorical_columns(data, categorical_cols)

    # Select numerical features for anomaly detection
    numerical_features = ['sid', 'classification', 'priority', 'protocol',
                      'source', 'destination', 'port', 'src_dest_count', 'events_per_min']

    # Ensure selected features exist in data
    data_numerical = data[numerical_features]

    # Normalize the features using StandardScaler
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data_numerical)


    # Train Isolation Forest
    iso_forest = IsolationForest(n_estimators=100, contamination=contamination, random_state=42)
    # Fit the model on scaled data
    iso_forest.fit(data_scaled)

    # Predict anomalies
    data['anomaly'] = iso_forest.predict(data_scaled)
    data['anomaly'] = data['anomaly'].map({1: 'Normal', -1: 'Anomaly'})

    anomalies_count = data['anomaly'].value_counts()
    anomalies = data[data['anomaly'] == 'Anomaly']

    return data, timestamp_column, anomalies_count, anomalies

def plot_anomalies_over_time(data, timestamp_column, figsize=(10,8)):
    # Visualize anomalies over time
    data['timestamp'] = pd.to_datetime(timestamp_column, errors='coerce')
    data.set_index('timestamp', inplace=True)
    data['anomaly_numeric'] = data['anomaly'].map({'Normal': 0, 'Anomaly': 1})
    fig, ax = plt.subplots(figsize=figsize)
    data['anomaly_numeric'].resample('1H').sum().plot(ax=ax)
    ax.set_title("Number of Anomalies Detected Per Hour")
    ax.set_ylabel("Number of Anomalies")
    ax.set_xlabel("Time")

    return fig