import pandas as pd
import numpy as np

# Homework 1
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
df.columns = [col.lower().replace(' ', '_') for col in df.columns]
print('First 3 rows:', df.head(3))
print('Mean age:', df['age'].mean())
print("Name and City columns:\n", df[['first_name', 'city']])
df['salary'] = np.random.randint(40000, 80000, size=len(df))
print('DataFrame with Salary:\n', df)
print('Summary statistics:\n', df.describe(include='all'))

# Homework 2
sales_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(sales_data)
print('Max Sales & Expenses:', sales_and_expenses[['Sales', 'Expenses']].max())
print('Min Sales & Expenses:', sales_and_expenses[['Sales', 'Expenses']].min())
print('Average Sales & Expenses:', sales_and_expenses[['Sales', 'Expenses']].mean())

# Homework 3
expense_data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}
expenses = pd.DataFrame(expense_data)
expenses_indexed = expenses.set_index('Category')
print('Max Expense per Category:\n', expenses_indexed.max(axis=1))
print('Min Expense per Category:\n', expenses_indexed.min(axis=1))
print('Average Expense per Category:\n', expenses_indexed.mean(axis=1))
