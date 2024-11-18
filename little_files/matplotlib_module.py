
import matplotlib.pyplot as plt
import pandas as pd

# Creating DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago'],
        'Courses': ['Maths', 'Geography', 'Accounting']}

df = pd.DataFrame(data)

print(df)
# Plotting Age vs. Name
plt.plot(df['Name'], df['Age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Name vs Age')
plt.show()

# Plotting a bar chart for Age by City
df.groupby('City')['Age'].mean().plot(kind='bar')
plt.xlabel('City')
plt.ylabel('Average Age')
plt.title('Average Age by City')
plt.show()

# Plotting a histogram for Age
df['Age'].plot(kind='hist', bins=10)
plt.xlabel('Age')
plt.title('Age Distribution')
plt.show()

# Plotting a scatter plot of Age vs. City
df.plot(kind='scatter', x='City', y='Age')
plt.title('City vs Age')
plt.show()

df['Age'].plot(kind='line', color='green', linestyle='--', linewidth=2)
plt.title('Age')
plt.show()