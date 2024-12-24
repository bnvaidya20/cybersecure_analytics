import pandas as pd
import gzip
import matplotlib.pyplot as plt


def load_cve_data(cve_file_path, encoding='utf-8'):
    try:
        with gzip.open(cve_file_path, 'rt', encoding=encoding) as f_in:
            cve_data = pd.read_csv(f_in)
        print(f"Successfully loaded data from {cve_file_path}")
        return cve_data
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
        print("Try using a different encoding (e.g., 'latin1').")
        return None
    except FileNotFoundError:
        print(f"Error: File {cve_file_path} not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def run_cve_analysis(cve_data):

    # Add a priority column based on cvss score
    def determine_priority(score):
        if score >= 9.0:
            return 'Critical'
        elif score >= 7.0:
            return 'High'
        elif score >= 4.0:
            return 'Medium'
        else:
            return 'Low'

    cve_data['Priority'] = cve_data['cvss'].apply(determine_priority)

    # Summary statistics
    priority_counts = cve_data['Priority'].value_counts()

    return priority_counts

def plot_priority_distribution(priority_counts, figsize=(10,8)):
    # Visualize priority distribution
    fig, ax = plt.subplots(figsize=figsize)
    priority_counts.plot(kind='bar', ax=ax, title='Vulnerability Priority Distribution')
    ax.set_xlabel('Priority Level')
    ax.set_ylabel('Number of Vulnerabilities')
    return fig