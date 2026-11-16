# Employee Salary Data Cleaning & Analysis

A simple Python project that loads employee data from CSV files, cleans it (removes duplicates, fills missing salaries), prints summary statistics, and plots a department-wise average salary chart.

## Features

- Reads employee data from a CSV file using **pandas**
- Removes duplicate rows
- Detects missing `Salary` values and fills them with the mean salary
- Prints a summary: number of employees, average salary, highest-paid employee, and total payroll
- Groups employees by department (count and average salary)
- Lists employees earning above 45,000
- Displays a bar chart: **Department-wise Average Salary**

## Requirements

- Python 3.8 or higher
- pandas
- matplotlib

Install the dependencies:

```bash
pip install pandas matplotlib
```

## Project Structure

```
.
├── main.py             # Main script (the code)
├── test_case1.csv      # Normal input
├── test_case2.csv      # Boundary / minimum input
├── test_case3.csv      # Invalid input (duplicates + missing salary)
└── README.md
```

> Note: rename `main.py` to whatever your script file is called.

## Input File Format

Each CSV file must contain at least these columns:

| Column       | Description                    |
|--------------|--------------------------------|
| `Name`       | Employee name                  |
| `Department` | Department the employee is in  |
| `Salary`     | Numeric salary (may be empty)  |

Example:

```csv
Name,Department,Salary
Amit,IT,50000
Neha,HR,42000
Ravi,IT,
Neha,HR,42000
```

## How to Run

1. Place all test CSV files in the same folder as the script.
2. Run:

```bash
python main.py
```

## How It Works

### `load_and_clean(filename)`

Loads the CSV and cleans it. Returns a tuple:

| Value         | Meaning                                   |
|---------------|-------------------------------------------|
| `df`          | Cleaned DataFrame                         |
| `duplicates`  | Number of duplicate rows removed          |
| `missing`     | Number of missing `Salary` values         |
| `mean_salary` | Mean salary used to fill the missing ones |

### `summary(df, show_total=True)`

Prints the employee count, average salary, and the highest-paid employee. If `show_total` is `True`, it also prints the total payroll.

## Test Cases

| # | Scenario                     | File             | What it shows                                                        |
|---|------------------------------|------------------|----------------------------------------------------------------------|
| 1 | Normal input                 | `test_case1.csv` | Full summary including total payroll                                 |
| 2 | Boundary / minimum input     | `test_case2.csv` | Summary without total payroll                                        |
| 3 | Invalid input                | `test_case3.csv` | Duplicates removed, missing salary filled with mean, cleaned rows    |
| 4 | Different valid scenario     | `test_case1.csv` | Department-wise stats, employees above 45,000, and the bar chart     |

## Output

The script prints results in the terminal for each test case. For Test Case 4, a bar chart window opens showing the average salary for each department.

## Possible Improvements

- Handle a missing `Salary` column or wrong file path with proper error messages
- Fill missing salaries with the department mean or median instead of the overall mean
- Make the salary threshold (45,000) configurable
- Save the chart as an image file instead of only displaying it

## License

This project is for learning and academic purposes.