# Masai_Personal_Expense_Tracker_Project
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal Expense Tracker - README</title>
</head>
<body>

<h1>Personal Expense Tracker</h1>
<p><strong>Language:</strong> Python</p>

<h2>Description:</h2>
<p>This is a simple Python-based command-line application designed to help you track your personal expenses. The application allows you to record and manage your expenses, view summaries, and search through past entries. All data is stored in a text file for persistence.</p>

<h2>Features:</h2>
<ol>
    <li><strong>Add Expense:</strong>
        <ul>
            <li>Record expenses by entering the category, amount, and date.</li>
            <li>Supports categories such as Food, Travel, Bus, etc.</li>
            <li>Validates amount and date inputs.</li>
        </ul>
    </li>
    <li><strong>View Expenses:</strong>
        <ul>
            <li>View all recorded expenses in a categorized and organized format.</li>
            <li>Displays expenses along with their category, amount, and date.</li>
        </ul>
    </li>
    <li><strong>Monthly Summary:</strong>
        <ul>
            <li>View total expenses for a specific month.</li>
            <li>Breaks down expenses by category and provides a total for each.</li>
        </ul>
    </li>
    <li><strong>Search Expenses:</strong>
        <ul>
            <li>Search for expenses by a keyword (category or date).</li>
            <li>Displays all matching entries for easy review.</li>
        </ul>
    </li>
    <li><strong>Delete Expense:</strong>
        <ul>
            <li>Allows you to delete an expense by entering the date.</li>
            <li>Displays matching expenses and prompts you to select the one to delete.</li>
        </ul>
    </li>
</ol>

<h2>How to Use</h2>
<ol>
    <li><strong>Clone the Repository:</strong>
        <p>Clone this repository to your local machine:</p>
        <pre>
git clone &lt;repository-url&gt;
cd &lt;repository-folder&gt;
        </pre>
    </li>
    <li><strong>Run the Application:</strong>
        <p>Run the application by executing the following command:</p>
        <pre>
python main.py
        </pre>
    </li>
    <li><strong>Choose an Option:</strong>
        <p>The program will display a menu with the following options:</p>
        <ul>
            <li>Add a new expense</li>
            <li>View recorded expenses</li>
            <li>View monthly summaries</li>
            <li>Search for expenses</li>
            <li>Delete an expense</li>
            <li>Exit the application</li>
        </ul>
    </li>
</ol>

<h2>Example Usage:</h2>

<h3>1. Adding an Expense:</h3>
<pre>
Enter category (e.g., Food, Travel, Bus): Food
Enter the amount: 15.75
Enter date (YYYY-MM-DD): 2025-01-01
Expense added successfully!
</pre>

<h3>2. Viewing Expenses:</h3>
<pre>
Expenses:
Food:
  1. Amount: 15.75 - Date: 2025-01-01
</pre>

<h3>3. Monthly Summary:</h3>
<pre>
Enter month and year (YYYY-MM): 2025-01
Monthly Summary (2025-01):
Total Expenses: 15.75
By Category:
  Food: 15.75
</pre>

<h3>4. Searching Expenses:</h3>
<pre>
Enter a keyword to search (e.g., category or date): Food
Food, 15.75, 2025-01-01
</pre>

<h3>5. Deleting an Expense:</h3>
<pre>
Enter the date of the expense to delete (YYYY-MM-DD): 2025-01-01
Matching expenses:
1. Food, 15.75, 2025-01-01
Enter the line number of the expense to delete: 1
Expense deleted successfully!
</pre>

<h2>File Structure:</h2>
<ul>
    <li><strong>main.py:</strong> The main script containing all application logic.</li>
    <li><strong>expenses_data1.txt:</strong> File where all expense data is stored.</li>
</ul>

<h2>Requirements:</h2>
<p>The application requires the following Python libraries:</p>
<ul>
    <li><strong>datetime:</strong> For working with date formats.</li>
    <li><strong>os:</strong> For file operations.</li>
</ul>
<p>No additional external libraries are required.</p>

<h2>License:</h2>
<p>This project is licensed under the MIT License.</p>

<h2>Author:</h2>
<p>Jagadish</p>

</body>
</html>

