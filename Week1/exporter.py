import csv
import json
import os

class Exporter:
    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def to_csv(self, data, filename="threats.csv"):
        path = os.path.join(self.output_dir, filename)

        if not data:
            print("No data to export (CSV)")
            return

        keys = data[0].keys()

        with open(path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

        print(f"CSV exported → {path}")

    def to_json(self, data, filename="threats.json"):
        path = os.path.join(self.output_dir, filename)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print(f"JSON exported → {path}")
