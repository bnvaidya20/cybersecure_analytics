

# Size of graph
SMALL_SIZE = (8, 5)
MEDIUM_SIZE = (10, 6)
LARGE_SIZE = (12, 8)

cicids_data_parts = [
    "datasets/normalized_cicids_data_part_1.jsonl.gz",
    "datasets/normalized_cicids_data_part_2.jsonl.gz",
    "datasets/normalized_cicids_data_part_3.jsonl.gz",
    "datasets/normalized_cicids_data_part_4.jsonl.gz"
]

MODEL_PATHS = {
    "Random Forest": "models/random_forest_model.pkl",
    "SVM": "models/svm_model.pkl"
}

ad_data_path = "datasets/cleaned_suricata_logs.yaml.gz"

json_path = "datasets/otx_pulses.json"

cve_file_path = 'datasets/normalized_cve_data.csv.gz'
