import json
import pandas as pd
import re


def load_json_data(json_path):
    # Load data from JSON file   
    with open(json_path, "r") as file:
        data = json.load(file)
    return data

def ioc_matching_module(data):

    # Extract relevant information from the JSON structure
    indicators = []
    for result in data["results"]:
        for indicator in result.get("indicators", []):
            indicators.append({
                "id": indicator.get("id"),
                "indicator": indicator.get("indicator"),
                "type": indicator.get("type"),
                "created": indicator.get("created"),
                "is_active": indicator.get("is_active"),
            })

    # Convert the extracted indicators to a DataFrame
    data_df = pd.DataFrame(indicators)

    # Rule-Based Matching Functions
    def is_ip(value):
        ip_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
        return bool(re.match(ip_pattern, value))

    def is_domain(value):
        domain_pattern = r"^([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
        return bool(re.match(domain_pattern, value))

    def is_hash(value):
        hash_pattern = r"^[a-fA-F0-9]{32}$|^[a-fA-F0-9]{40}$|^[a-fA-F0-9]{64}$|^[a-fA-F0-9]{128}$"
        return bool(re.match(hash_pattern, value))

    def is_url(value):
        url_pattern = r"^(http|https):\/\/[a-zA-Z0-9.-]+(:[0-9]+)?(\/[a-zA-Z0-9-._~:/?#[\]@!$&'()*+,;=]*)?$"
        return bool(re.match(url_pattern, value))

    def is_cve(value):
        cve_pattern = r"^CVE-\d{4}-\d{4,7}$"
        return bool(re.match(cve_pattern, value))

    # Apply rules to classify indicators
    def classify_ioc(row):
        value = row['indicator']
        if is_ip(value):
            return 'IP Address'
        elif is_domain(value):
            return 'Domain'
        elif is_hash(value):
            return 'Hash'
        elif is_url(value):
            return 'URL'
        elif is_cve(value):
            return 'CVE'
        else:
            return 'Unknown'

    # Add a new column for IoC classification
    data_df['ioc_type'] = data_df.apply(classify_ioc, axis=1)

    # Summary of IoC counts by type
    ioc_summary = data_df['ioc_type'].value_counts()

    return data_df, ioc_summary

# Filter based on IoC types 
def filter_iocs(data_df, ioc_type):
    return data_df[data_df['ioc_type'] == ioc_type]