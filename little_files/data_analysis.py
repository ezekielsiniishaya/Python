# Importing pandas framwork for data analysis
import pandas as pd
# Importing matplotlib for visual diagrams
import matplotlib.pyplot as plt
# File handling and  Loading a csv file to the program and storing it in a variable called data, specifying that the separator is ; not ,

try:
    data = pd.read_csv('student-mat.csv', sep =";")
except FileNotFoundError:
    print("Error: The file was not found. Please check the file path.")
except pd.errors.ParserError:
    print("Error: The file format is incorrect. Ensure it is a valid CSV.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# Converting the csv file into a dataframe
df = pd.DataFrame(data)
# Display the first few rows of the dataset using .head() to inspect the data
print(df.head())
# Checking the structure of the dataset and any missing values
print(df.info())
print(df.isnull())

print(df.describe())  # Provides summary statistics for numerical columns

# Cleaning the data by dropping any rows with missing values
df = df.dropna()

print(df.isnull().sum())  # Verify there are no missing values
# Perfoming basic statistics on numerical column
print(df['age'].describe())

# Grouping the data
print(df.groupby('Fjob')['age'].mean())

# I have observed that the fathers that stay at home have older children compared to fathers that go to work


# Plotting a line graph of father's job over health

df.groupby('age')['health'].mean().plot(kind='line', color='green', linestyle='-', linewidth=2)
plt.title('Age Vs Average Health')
plt.xlabel('Age')
plt.ylabel('Average Health')
plt.show()

# A bar chart to show number of absences in relation to free time

df.groupby('absences')['freetime'].mean().plot(kind='bar', color='red', linewidth=5)
plt.title('Absences vs Freetime')
plt.xlabel('Average freetime')
plt.ylabel('Absences')
plt.show()

# Plotting a histogram for Age  
df['age'].plot(kind='hist')
plt.xlabel('Age')
plt.title('Age Distribution')
plt.show()

# Plotting a scatter plot for age vs. freetime
df.plot(kind='scatter', x='freetime', y='age')
plt.title('Freetime vs Age')
plt.show()