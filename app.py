

import sqlite3
from datetime import datetime
import os

from seasonal_flavors import manage_seasonal_flavors
from ingredient_base import manage_ingredient_inventory
from suggestions import manage_customer_suggestions

DB_NAME = 'inventory.db'

def establish_db_connection():

    return sqlite3.connect(DB_NAME)

def initialize_database(connection):

    with connection:
        db_cursor = connection.cursor()  # Changed from db_vs() to cursor()
        
        db_cursor.execute('''
        CREATE TABLE IF NOT EXISTS seasonal_flavors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            season TEXT NOT NULL,
            description TEXT
        )
        ''')
        
        db_cursor.execute('''
        CREATE TABLE IF NOT EXISTS ingredient_inventory (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            quantity REAL NOT NULL,
            unit TEXT NOT NULL
        )
        ''')
        
        db_cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer_suggestions (
            id INTEGER PRIMARY KEY,
            flavor_name TEXT NOT NULL,
            description TEXT,
            allergy_concerns TEXT,
            submission_date TEXT NOT NULL
        )
        ''')

def display_main_menu():
    """Display the main menu options to the user."""
    print("\nChocolate House Manage")
    print("1. Management of Seasonal Flavors")
    print("2. Management of Ingredient base")
    print("3. Management of Customer Suggestions")
    print("4. Exit")

def process_user_choice(choice, connection):

    if choice == '1':
        manage_seasonal_flavors(connection)
    elif choice == '2':
        manage_ingredient_inventory(connection)
    elif choice == '3':
        manage_customer_suggestions(connection)
    elif choice == '4':
        print("Thank you")
        return False
    else:
        print("Invalid choice")
    return True

def run_application():

    connection = establish_db_connection()
    initialize_database(connection)
    
    application_running = True
    while application_running:
        display_main_menu()
        user_choice = input("Enter your choice between (1-4): ")
        application_running = process_user_choice(user_choice, connection)
    
    connection.close()

if __name__ == "__main__":
    run_application()
