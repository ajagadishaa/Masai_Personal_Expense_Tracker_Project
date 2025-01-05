# Masai_Personal_Expense_Tracker_Project
Project Name: Personal Expense Tracker
Language:Python

Description:
This is a simple Python-based command-line application designed to help you track your personal expenses. The application allows you to record and manage your expenses, view summaries, and search through past entries. All data is stored in a text file for persistence.

Features: 
1. Add Expense:
Record expenses by entering the category, amount, and date.
Supports categories such as Food, Travel, Bus, etc.
Validates amount and date inputs.

2. View Expenses:
View all recorded expenses in a categorized and organized format.
Displays expenses along with their category, amount, and date.

3. Monthly Summary:
View total expenses for a specific month.
Breaks down expenses by category and provides a total for each.

4. Search Expenses:
Search for expenses by a keyword (category or date).
Displays all matching entries for easy review.

6. Delete Expense
Allows you to delete an expense by entering the date.
Displays matching expenses and prompts you to select the one to delete.

How to Use
1. Clone the Repository
Clone this repository to your local machine:

git clone <repository-url>
cd <repository-folder>

2. Run the Application
Run the application by executing the following command:

python main.py

3. Choose an Option:
The program will display a menu with the following options:

Add a new expense
View recorded expenses
View monthly summaries
Search for expenses
Delete an expense
Exit the application

Example Usage: 

1.Adding an Expense:
Enter category (e.g., Food, Travel, Bus): Food
Enter the amount: 15.75
Enter date (YYYY-MM-DD): 2025-01-01
Expense added successfully!

2.Viewing Expenses:
Expenses:
Food:
  1. Amount: 15.75 - Date: 2025-01-01
     
3.Monthly Summary:
Enter month and year (YYYY-MM): 2025-01
Monthly Summary (2025-01):
Total Expenses: 15.75
By Category:
  Food: 15.75
  
4.Searching Expenses:
Enter a keyword to search (e.g., category or date): Food
Food, 15.75, 2025-01-01

5.Deleting an Expense:
Enter the date of the expense to delete (YYYY-MM-DD): 2025-01-01
Matching expenses:
1. Food, 15.75, 2025-01-01
Enter the line number of the expense to delete: 1
Expense deleted successfully!

File Structure:
main.py: The main script containing all application logic.
expenses_data1.txt: File where all expense data is stored.

Requirements:
The application requires the following Python libraries:
datetime: For working with date formats.
os: For file operations.
No additional external libraries are required.

License
This project is licensed under the MIT License

Author
Jagadish
