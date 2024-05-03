# Author: Ryan Deyo
# Date: 5/2/2024
# Description: Script for removing user selected keys and the corresponding data from a JSON file

import json
import sys

def main():
    fileName = input("Please enter the json file you would like to clean (include \".json\"): ")


    # Load the JSON data from the json file
    with open(fileName, encoding='utf-8') as file:
        data = json.load(file)
    
    while True:
        # Get the keys into a list, removing duplicates
        keys = list(set(get_json_keys(data)))       
        # Key Menu
        print("Keys:")
        for i in keys:
            print(i)

        response = input("Please input a key to wipe from the file. If more than one key please separate with commas (case sensitive): ")
        
        # Splits the response into a list to account for any number of keys inputted
        response_list = [key.strip() for key in response.split(',')]
        
        if response_list:
            for i in response_list:
                remove_json_key(data, i)
        
        # Ask user if they want to clean more data
        choice = input("Would you like to clean more data? (Y/N): ").lower() 
        if choice == "y":
            pass
        if choice == "n":
            # Creates a new json file with the same name as the original with "cleaned_" infront of it
            with open("cleaned_"+fileName,"w") as file:
                json.dump(data, file, indent=2)

            print("The file " + "\"cleaned_" + fileName + "\" has been created.")
            sys.exit()

# Recursively gets all the keys in the JSON file (including duplicates) 
def get_json_keys(data):
    keys = []
    # If the data is a dictionary
    if isinstance(data, dict):
        keys += data.keys()
        for key, value in data.items():
            # Iterate over each key-value pair in the dictionary 'data'
            # 'key' represents the key of the current pair
            # 'value' represents the corresponding value of the current pair
            keys += get_json_keys(value)
    # If the data is a list
    elif isinstance(data, list):
        for item in data:
            keys += get_json_keys(item)
    return keys

# Recursively removes the specified key from the JSON data
def remove_json_key(data, targetKey):
    # If the data is a dictionary
    if isinstance(data, dict):
        if targetKey in data:
            del data[targetKey]
        for key, value in data.items():
            # Iterate over each key-value pair in the dictionary 'data'
            # 'key' represents the key of the current pair
            # 'value' represents the corresponding value of the current pair
            remove_json_key(value, targetKey)
    # If the data is a list
    elif isinstance(data, list):
        for item in data:
            remove_json_key(item, targetKey)

if __name__ == "__main__":
    main()