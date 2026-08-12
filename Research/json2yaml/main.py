import argparse
import os
import sys

# Ensure the parent directory is in the path to import json2yaml
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from json2yaml import convert_json_to_yaml

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert JSON game file to YAML format using the modular system.")
    parser.add_argument("json_input_file", help="Path to the input JSON file.")
    args = parser.parse_args()

    json_filepath = args.json_input_file
    
    # Derive output YAML filename
    base_name, _ = os.path.splitext(os.path.basename(json_filepath))
    output_filepath = os.path.join(os.path.dirname(json_filepath), f"{base_name}.yaml")

    convert_json_to_yaml(json_filepath, output_filepath)
    print(f"Successfully converted {json_filepath} to {output_filepath}")
