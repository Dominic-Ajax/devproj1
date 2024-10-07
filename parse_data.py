import json
import xmltodict
import yaml

def parse_json(data):
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None

def parse_xml(data):
    try:
        return xmltodict.parse(data)
    except Exception as e:
        print(f"Error parsing XML: {e}")
        return None

def parse_yaml(data):
    try:
        return yaml.safe_load(data)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return None
