import pandas as pd
import json


def excel_to_json(excel_file_path, sheet_name=0):
    """
    Convert an Excel file to JSON format.

    Parameters:
    - excel_file_path: str, path to the Excel file.
    - sheet_name: str or int, name or index of the sheet to read. Defaults to the first sheet.

    Returns:
    - json_data: str, JSON representation of the Excel sheet.
    """
    # Read the Excel file
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

    # Convert the DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data


# Example usage
excel_path = 'docs/IS_OTC_DRUG.xlsx'  # Make sure to update this path to your actual Excel file path
json_output = excel_to_json(excel_path)
#print(json_output)


# Parse the JSON string into a Python object
data = json.loads(json_output)

# Loop through the list (if the root is a list)
for obj in data:
    print(obj)
    # If you want to access specific fields, you can do so like this:
    # print(f"Name: {obj['Name']}, Age: {obj['Age']}, City: {obj['City']}")
