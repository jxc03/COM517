'''
This  generates a JSON dataset of 15 users with typical Northern Ireland names and cities.
Each user has a first and last name, an age between 18 and 55, and a city in Northern Ireland.
The generated dataset is saved to a file named 'users.json'.
'''

import json # Imports JSON module to work with JSON data
import random # Imports random module to generate the data

# Sample data with typical Northern Ireland names
first_names = ["Eoin", "Niamh", "Aoife", "Conor", "Siobhan", "Ciaran", "Ciara", "Padraig", "Aine", "Rory", "Orla", "Sean", "Maeve", "Colm", "Aisling"]  # List of first names
last_names = ["O'Neill", "Gallagher", "Maguire", "Murphy", "O'Donnell", "McLaughlin", "O'Doherty", "Byrne", "Doherty", "McCormack", "Lynch", "McKenna", "Fitzpatrick", "McCarthy", "Campbell"]  # List of last names

# Sample data with Northern Ireland cities
cities = ["Belfast", "Derry", "Lisburn", "Newry", "Armagh", "Ballymena", "Bangor", "Coleraine", "Newtownabbey", "Carrickfergus", "Antrim", "Omagh", "Londonderry", "Portadown", "Cookstown"]  # List of cities in Northern Ireland

# Generates dataset
users = []  # Initializes an empty list to store the user data
for _ in range(15):  # Loop to create 15 users
    user = { # Dictionary to store the user information
        "name": f"{random.choice(first_names)} {random.choice(last_names)}",  # Randomly chooses a first and last name
        "age": random.randint(18, 55),  # Randomly assigns an age between 18 and 55
        "city": random.choice(cities)  # Randomly chooses a city
    }
    users.append(user)  # Adds the user to the list

# Saves the data to a JSON file
try: # Start of the try block for exception handling
    with open('users.json', 'w') as file:  # Opens a file for writing
        json.dump(users, file, indent=4)  # Writes the list of users to the file with an indentation of 4 spaces
    print("JSON dataset created successfully!")  # Prints success message
except Exception as e:  # Catches any exceptions that occurs
    print(f"An error occurred: {e}")  # Prints the error message


