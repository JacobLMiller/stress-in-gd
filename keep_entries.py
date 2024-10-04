import json
import os

def load_json(file_path):
    """Load the JSON file containing a list."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []
    except json.JSONDecodeError:
        print("Error: The JSON file is malformed.")
        return []

def write_json(file_path, data):
    """Write the kept entries to a JSON file."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

import os
def process_entries(input_file, output_file):
    """Iterate over each entry in the list and ask the user to keep or delete."""
    data = load_json(input_file)
    if not data:
        return
    
    kept_entries = []

    # Process each entry in the list
    for entry in data:
        os.system("clear")
        print(f"\nEntry: {entry}")
        action = input("Do you want to keep this entry? (yes/no): ").strip().lower()

        if action == 'yes' or action == 'y':
            kept_entries.append(entry)
            write_json(output_file, kept_entries)
            print(f"Entry kept. Current kept entries saved to {output_file}.")
        else:
            print("Entry deleted.")

    print("\nProcessing complete. Final kept entries:")
    print(kept_entries)

if __name__ == "__main__":
    # Input and output file paths
    input_file = 'ref-list.json'  # Replace with the path to your input JSON file
    output_file = 'kept_entries.json'  # Replace with the path to the output JSON file

    process_entries(input_file, output_file)