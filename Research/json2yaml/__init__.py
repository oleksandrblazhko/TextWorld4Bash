from .converter import convert_json_data_to_yaml_dict
from .formatter import format_yaml
import json

def convert_json_to_yaml(json_filepath, output_filepath):
    """
    Converts a TextWorld game JSON file to a beautifully structured YAML file
    following the standard human-readable template.
    """
    with open(json_filepath, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        
    output_dict, room_name_map = convert_json_data_to_yaml_dict(json_data)
    yaml_str = format_yaml(output_dict, room_name_map)
    
    with open(output_filepath, 'w', encoding='utf-8') as f:
        f.write(yaml_str)
