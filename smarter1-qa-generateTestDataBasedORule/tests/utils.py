import pandas as pd


def load_excel_to_json(file_path):
    """Reads an Excel file and converts it to a list of JSON objects."""
    df = pd.read_excel(file_path, engine='openpyxl')
    json_objects = df.to_dict(orient='records')
    return json_objects
