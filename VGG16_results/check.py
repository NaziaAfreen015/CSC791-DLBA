import json


def read_json_file(filename):
    """Reads a JSON file and returns the data as a Python object."""
    table_titles = []
    try:
        # Open the file in read mode ('r')
        with open(filename, 'r') as file:
            # Load the JSON data and store it in a Python variable (e.g., 'data')
            data = json.load(file)
            
        # Now you can work with the 'data' variable as a standard Python object
        print(f"Data successfully loaded from {filename}!")
        print(f"Type of data: {type(data)}")
        print(len(data))
        for table in data:
            table_titles.append(table['title'])
        
        return table_titles

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file. Check for invalid JSON content.")


# The name of your JSON file
filename = 'VGG16_T1_C100_result.json'
# Call the function to read the JSON file
table_titles1 = read_json_file(filename)

filename = 'VGG16_T1_C10_result.json'
table_titles2 = read_json_file(filename)

# compare the two lists of table titles
if table_titles1.sort() == table_titles2.sort():
    print("The table titles in both JSON files are the same.")
else:    print("The table titles in both JSON files are different.")