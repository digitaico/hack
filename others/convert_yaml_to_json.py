import yaml
import json
import os

def validate_file(file_path):
    """Validate that file exists and is not empty"""
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return False
    if os.path.getsize(file_path) == 0:
        print(f"Error: File '{file_path}' is empty.")
        return False
    return True

def extract_fields(data, fields):
    """ Extract specified fields from the YAML structure"""
    extracted = []
    # Check if data is a list
    if isinstance(data, list):
        for item in data:
            extracted_item = {}
            for field in fields:
                keys = field.split(".") # to handle nested fields
                value = item
                for key in keys:
                    value = value.get(key) if isinstance(value, dict) else None

                # convert value to hex
                if field.endswith("value") and isinstance(value, int):
                    value = f"0x{value:04X}" # convert to hexadecimal
                extracted_item[field] = value
            extracted.append(extracted_item)
    elif isinstance(data, dict):
        extracted_item= {}
        for field in fields:
            keys = field.split(".") # to handle nested fields
            value = data
            for key in keys:
                value = value.get(key) if isinstance(value, dict) else None

            # convert value to hex
            if field.endswith("value") and isinstance(value, int):
                #value = hex(value) # convert to hexadecimal
                value = f"0x{value:04X}" # convert to hexadecimal
            extracted_item[field] = value
        extracted.append(extracted_item)
    return extracted

def extract_and_convert(yaml_file, json_file, fields):
    try:
        # Load the YAML file
        with open(yaml_file, 'r') as yf:
            yaml_raw = yf.read()
        # parse YAML to ensure values remain strings
        yaml_data = yaml.safe_load(yaml_raw)

        # Extract specified fields
        extracted_data = extract_fields(yaml_data.get("company_identifiers",[]), fields)

        # Save the extracted data as JSON
        with open(json_file, 'w') as jf:
            json.dump(extracted_data, jf, indent=4)

        print(f"Data successfully extracted and saved to {json_file}")
    except yaml.YAMLError:
        print("Error: Invalid YAML file format")
    except Exception as e:
        print(f"An error ocurred: {e}")

def main():
    try:
        # prompt user for input and output files
        yaml_file = input("What yaml file? ").strip()
        json_file = input("Name of json output file: ").strip()

        # Validate input file
        if not validate_file(yaml_file):
            return

        # prompt user for fields to extract
        fields = input("Enter the fields to extract, comma separated: ").strip().split(',')

        if len(fields) == 0:
            print("Error: No fields provided for extraction.")
            return

        # Perform extraction and conversion
        extract_and_convert(yaml_file, json_file, fields)
    except KeyboardInterrupt:
        print("\nOperation canceled by user.")

if __name__ == "__main__":
    main()
