import numpy as np
import pandas as pd
import gzip

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

import warnings
from sklearn.exceptions import InconsistentVersionWarning

warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

# Function to load the dataset
def load_ids_data(cicids_data_parts):
    # List to hold decompressed data
    combined_data = []

    for part in cicids_data_parts:
        print(f"Processing: {part}")
        # Decompress the Gzip file
        with gzip.open(part, 'rt') as f_in:
            # Load the JSONL part into a DataFrame
            part_data = pd.read_json(f_in, orient="records", lines=True)
            combined_data.append(part_data)

    # Combine all parts into a single DataFrame
    combined_data = pd.concat(combined_data, ignore_index=True)
    print(f"Combined dataset shape: {combined_data.shape}")

    # Separate features (X) and labels (y)
    X = combined_data.drop(columns=['Label'])  
    y = combined_data['Label']
    return X, y

# Function to load the model
def load_model(model_path):
    """
    Load the pre-trained model from a file.
    """
    try:
        model = joblib.load(model_path)
        print("Model loaded successfully!")
        return model
    except FileNotFoundError:
        print("Error: Model file not found.")
    except Exception as e:
        print(f"An error occurred while loading the model: {e}")
    return None

# Function to evaluate the model
def evaluate_model(model, X, y):
    """
    Evaluate the model on the provided dataset.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    cm = confusion_matrix(y_test, predictions)
    report = classification_report(y_test, predictions, zero_division=0)
    return accuracy, cm, report

# Function to plot confusion matrix
def plot_confusion_matrix(cm, figsize=(10, 8), title="Confusion Matrix"):
    """Plot a confusion matrix as a heatmap."""
    cm_percentage = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(
        cm_percentage, 
        annot=True, 
        fmt=".2f", 
        cmap="Reds", 
        cbar_kws={'label': 'Percentage (%)'}
    )
    plt.title(title)
    plt.xlabel("Predicted Labels")
    plt.ylabel("True Labels")
    return fig


def plot_feature_importance(model, feature_names, figsize=(10, 8), top_n=10):

    """Plot the top N important features."""
    feature_importance = pd.Series(model.feature_importances_, index=feature_names).sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=figsize)
    feature_importance.head(top_n).plot(kind='bar', title=f'Top {top_n} Feature Importance', ax=ax)
    plt.ylabel("Importance Score")
    return fig