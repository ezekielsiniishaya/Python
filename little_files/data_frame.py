import pandas as pd

# Creating DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago'],
        'Courses': ['Maths', 'Geography', 'Accounting']}

df = pd.DataFrame(data)

print(df['Age'].mean())