# Python-Challenge
Py_Bank Financial Analysis
This Python script analyzes financial data from a CSV file containing date and profit/loss columns.

Description
This script calculates various financial statistics based on the data provided in the budget_data.csv file located in the Py_Bank/Resources directory. It computes the total number of months included in the dataset, the net total amount of "Profit/Losses" over the entire period, the average of the changes in "Profit/Losses" over the entire period, and identifies the greatest increase and decrease in profits along with their respective dates.

How to Use
Prerequisites
Python 3.x
CSV file named budget_data.csv containing columns: Date, Profit/Losses
Instructions
Clone the repository to your local machine.
Place the budget_data.csv file inside the Py_Bank/Resources directory.
Run the script financial_analysis.py.
bash
Copy code
python financial_analysis.py
View the financial analysis results displayed in the console.
The script will generate a Financial_Output.txt file in the Py_Bank/Resources directory containing the same analysis output.
Output
The script will display the following information in the console:

Total months included in the dataset.
Total "Profit/Losses" over the entire period.
Average of the changes in "Profit/Losses" over the entire period.
Greatest increase in profits with the corresponding date.
Greatest decrease in profits with the corresponding date.
Additionally, it generates a Financial_Output.txt file containing the same information for further reference.
