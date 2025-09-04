# personal-expense-tracker
A Personal Expense Tracker built in 3 phases: CLI, Streamlit, and Flask/Django.

## Personal Expense Tracker (CLI)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub stars](https://img.shields.io/github/stars/yourusername/personal-expense-tracker?style=social)

---

## 🚀 Overview  
This is a **Command Line Interface (CLI)** project that helps users manage and track their daily expenses.  
It supports multiple users, stores data in CSV files, and provides basic CRUD operations.  

---

## ✨ Features  
- 👤 **User Accounts** – Create a personal CSV file (`username_expense.csv`).  
- ➕ **Add Expenses** – Save date, category, and amount.  
- 📖 **View Expenses** – Display all records in a table.  
- ❌ **Delete Expenses** – Remove entries using an index number.  
- 📂 **File Handling** – Data stored in per-user CSV files.  
- 🛠 **Argparse** – Command-based usage (`add`, `view`, `delete`, etc.).  

---

## 🛠 Technologies Used  
- **Python** (CLI application)  
- **CSV Module** (file handling)  
- **Argparse** (command-line argument parsing)  
- **Datetime** (handling expense dates)  

---

## ▶️ How to Run  
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/personal-expense-tracker.git
   cd personal-expense-tracker

# Sign in / Register
python expense_tracker.py signin --name Your_name

# Log in
python expense_tracker.py login --name Your_name

# Add expense
python expense_tracker.py add --category Travel --amount 250

# View expenses
python expense_tracker.py view

# Delete expense
python expense_tracker.py delete

# Update expense
python expense_tracker.py update