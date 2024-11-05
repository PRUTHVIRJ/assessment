###### 🍫Chocolate House Management System
A simple Python application designed to manage seasonal flavors, ingredient inventory, and customer feedback, perfect for a fictional chocolate house. The system utilizes SQLite for data storage, allowing efficient and reliable management.

### 📋Problem Statement
Develop a user-friendly application for a fictional chocolate house to manage:
* Seasonal Chocolate Flavors
* Ingredient Inventory
* Customer Flavor Suggestions and Allergy Concerns

### 🌟Key Features
1.Seasonal Flavor Management: Easily add, view, update, or remove seasonal chocolate flavors.
2.Ingredient Inventory Tracking: Maintain up-to-date ingredient records, adjust quantities, and remove items as needed.
3.Customer Suggestions: Store customer feedback, including flavor ideas and allergy concerns.
4.Data Persistence with SQLite: All records are saved in an SQLite database, ensuring data is preserved across sessions.

### 🛠Requirements
Python 3.6+
SQLite3 (typically included with Python)

### 📁Project Layout
The project files are organized as follows:
chocolate_house_app.py - Core file that initializes and runs the application.
seasonal_flavors.py - Module for managing seasonal chocolate flavor records.
ingredient_inventory.py - Module to handle ingredient inventory tasks.
customer_suggestions.py - Module for storing and managing customer suggestions.
chocolate_house.db - SQLite database file created automatically on first run.

### 🚀Setup & Installation
Clone or Download the project repository.
Open a terminal and navigate to the project folder.

### ▶️ Running the Application
To start the application:
Open a terminal or command line window.
Navigate to the folder containing the project files.

Use this command to run the application:
```
python app.py
```
For Python 3, you may need to use:
````
python3 app.py
```
The main menu will display options for managing flavors, ingredients, and customer feedback.

### 📖Application Guide

Menu Options
The main menu presents options to manage each aspect of the chocolate house:

1.Manage Seasonal Flavors
2.Manage Ingredient Inventory
3.Manage Customer Suggestions
4.Exit Application
Select option 4 to exit the program.

### 🧪Testing Instructions
Use these test cases to ensure the application functions correctly.

### Main Menu
Verify that selecting each option (1-4) opens the corresponding module or exits the application.

### Seasonal Flavors Management
Add a seasonal flavor and confirm it appears in the list.
Update a flavor and check that changes are saved.
Delete a flavor and verify its removal from the list.

### Ingredient Inventory Management
Add an ingredient and confirm it’s displayed in the inventory.
Update the quantity of an existing ingredient and verify the update.
Remove an ingredient and check that it no longer appears in the inventory.

### Customer Suggestions Management
Add a customer suggestion and confirm it’s recorded.
View the list of suggestions and ensure the new entry is present.
Delete a suggestion and check that it’s removed.

### Data Persistence
Exit and restart the application.
Confirm that all previously added data for flavors, ingredients, and suggestions is still available.

### Error Handling & Validation
Test the response to invalid inputs (e.g., entering letters instead of numbers).
Try updating or deleting non-existent entries to confirm appropriate error messages.

### Database Verification
Use a SQLite browser to open the chocolate_house.db file.
Confirm that the database tables (seasonal_flavors, ingredient_inventory, customer_suggestions) are correctly structured.
Verify that the data in the database matches what appears in the application.
