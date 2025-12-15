import csv
import json
import os

def csv_to_json(csv_file_path, json_file_path):
    """
    Convert CSV file to JSON file
    """
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"{csv_file_path} not found")

    data = []

    with open(csv_file_path, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)

    with open(json_file_path, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

    return f"CSV converted to JSON successfully: {json_file_path}"
