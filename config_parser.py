import configparser
import json
from flask import Flask, jsonify

# Flask app for handling the GET request
app = Flask(__name__)

def parse_config_file(file_path):
    """
    Parse a configuration file and return the extracted key-value pairs as a dictionary.
    :param file_path: Path to the configuration file.
    :return: Dictionary containing the parsed configuration data.
    """
    config = configparser.ConfigParser()
    try:
        # Attempt to read the configuration file
        config.read(file_path)

        # Parse the configuration file into a dictionary
        parsed_data = {section: dict(config.items(section)) for section in config.sections()}
        return parsed_data
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file '{file_path}' not found.")
    except configparser.Error as e:
        raise ValueError(f"Error parsing configuration file: {e}")


def save_to_json(data, output_file):
    """
    Save dictionary data to a JSON file.
    :param data: Dictionary to save.
    :param output_file: Path to the output JSON file.
    """
    try:
        with open(output_file, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"✅ Data successfully saved to {output_file}.")
    except Exception as e:
        print(f"❌ Error saving data to JSON file: {e}")


@app.route('/config', methods=['GET'])
def get_config_data():
    """
    Handle GET requests to fetch configuration data.
    :return: JSON response containing the configuration data.
    """
    try:
        # Read data from the saved JSON file
        with open('config_data.json', 'r') as json_file:
            data = json.load(json_file)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Configuration file path
    config_file_path = "config.ini"  # Sample configuration file path
    output_json_file = "config_data.json"  # File to store parsed JSON data

    try:
        # Parse the configuration file
        print("Parsing configuration file...")
        config_data = parse_config_file(config_file_path)
        print("Parsed Configuration Data:")
        for section, values in config_data.items():
            print(f"{section}:")
            for key, value in values.items():
                print(f"  - {key}: {value}")

        # Save parsed data as JSON
        save_to_json(config_data, output_json_file)

        # Start the Flask server
        print("Starting the Flask server...")
        app.run(port=5000)  # Server runs on http://127.0.0.1:5000
    except Exception as e:
        print(f"❌ Error: {e}")
