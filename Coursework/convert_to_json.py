'''
import pandas as pd
import json

input_csv = 'dataset_csv.csv'
output_json = 'dataset_json.json'

def change_tags_field(tags_string):
    if tags_string:
        return [tag.strip() for tag in tags_string.split(',')]
    return []

def change_reviewer_details(details_string):
    if details_string:
        parts_of_detail = [part.strip() for part in details_string.split(',')]
        details = {}
        for part in parts_of_detail:
            attribute_name, attribute_value = part.split(':', 1)
            details[attribute_name.strip()] = attribute_value.strip()
        return details
    return{}

def change_resolve_to_boolean(value):
    return value.strip().lower == 'yes'

def convert_csv_to_json(input_csv, output_json):
    with open(input_csv, mode = 'r') as file:
        lines = file.readlines()
        headers = [header.strip() for header in lines[0].split(',')]   
        data = []
        for line in lines[1:]:
            data_values = [value.strip() for value in line.split(',')]
            row = {}
            for i in range(len(headers)):
                row[headers[i]] = data_values[i] if i < len(data_values) else None
            row['Tags'] = change_tags_field(row['Tags'])
            row['Reviewer Details'] = change_reviewer_details(row['Reviewer Details'])
            row['Resolved'] = change_resolve_to_boolean(row['Resolved'])
            data.append(row)
    with open(output_json, mode='w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"JSON file has been successfully saved to {output_json}")

convert_csv_to_json(input_csv, output_json)
'''

import pandas as pd
import json

#input_csv = 'dataset_csv.csv'
input_csv = 'C:/Users/jcari/Documents/COM517-1/Coursework/dataset_csv.csv'
output_json = 'dataset_jsonVideo.json'

# Change tag field
def change_tags_field(tags_string):
    return [tag.strip() for tag in tags_string.split(',')] if tags_string else []

# Coverted reviewer details into a dictionary
def change_reviewer_details(details_string):
    if details_string:
        parts_of_detail = [part.strip() for part in details_string.split(',')]
        details = {}
        for part in parts_of_detail:
            attribute_name, attribute_value = part.split(':', 1)
            details[attribute_name.strip()] = attribute_value.strip()
        return details
    return {}

#Convert Yes/No to boolean True/False.
def change_resolve_to_boolean(value):
    return value.strip().lower() == 'yes' if value else False

def convert_csv_to_json(input_csv, output_json):
    # Read the CSV file
    df = pd.read_csv(input_csv, encoding='utf-8')
    
    # Apply transformations to specific columns
    if 'Tags' in df.columns:
        df['Tags'] = df['Tags'].apply(change_tags_field)
    if 'Reviewer Details' in df.columns:
        df['Reviewer Details'] = df['Reviewer Details'].apply(change_reviewer_details)
    if 'Resolved' in df.columns:
        df['Resolved'] = df['Resolved'].apply(change_resolve_to_boolean)

    # Replace NaN values with None in the 'Resolution Date' column (or other columns if needed)
    if 'Resolution Date' in df.columns:
        df['Resolution Date'] = df['Resolution Date'].where(df['Resolution Date'].notna(), None)
        
    # Convert DataFrame to a JSON-compatible format (list of dictionaries)
    data = df.to_dict(orient='records')
    
    # Write the JSON data to a file
    with open(output_json, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"JSON file has been successfully saved to {output_json}")

# Execute the conversion function
convert_csv_to_json(input_csv, output_json)
