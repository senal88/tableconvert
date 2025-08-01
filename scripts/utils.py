import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TABLECONVERT_API_KEY")
API_URL = "https://api.tableconvert.com"


def get_input_path(file_type):
    """
    Prompts the user to enter the input file path, with a default path provided.

    Args:
        file_type (str): The type of file to be converted (e.g., 'excel', 'json').

    Returns:
        str: The path to the input file.
    """
    default_path = os.path.join("data", "input", file_type)
    input_path = input(
        f"Enter the path to the {file_type} file (default: {default_path}): "
    )
    if not input_path:
        return default_path
    return input_path


def convert_file(input_path, conversion_type):
    """
    Calls the TableConvert API to convert a file.

    Args:
        input_path (str): The path to the input file.
        conversion_type (str): The type of conversion to perform (e.g., 'excel-to-json').

    Returns:
        str: The converted data, or None if the conversion fails.
    """
    if not API_KEY:
        print("Error: TABLECONVERT_API_KEY not found in .env file.")
        return None

    headers = {"Authorization": f"Bearer {API_KEY}"}

    with open(input_path, "rb") as f:
        files = {"data": f}
        response = requests.post(
            f"{API_URL}/{conversion_type}", headers=headers, files=files
        )

    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        print(response.text)
        return None
