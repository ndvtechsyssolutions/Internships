# COVID Dataset Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
covid_path = 'covid_data.csv'
covid_df = pd.read_csv(covid_path)

# Handle missing values
covid_df.fillna({'continent': "Unknown"}, inplace=True)
covid_df = covid_df.fillna(covid_df.mean(numeric_only=True))

# Display dataset after preprocessing
print("COVID Data Summary:\n")
print(covid_df.describe())
print("\nFirst 5 rows:\n")
print(covid_df.head())

# Visualizations

# 1️⃣ Bar plot: Cases by continent
plt.figure(figsize=(8, 5))
sns.countplot(data=covid_df, x='continent', palette='Set2')
plt.title("Number of Cases by Continent")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2️⃣ Line plot: Life Expectancy vs Male Smokers
plt.figure(figsize=(8, 5))
sns.lineplot(x=covid_df['male_smokers'], y=covid_df['life_expectancy'], color='blue')
plt.title("Life Expectancy vs Male Smokers")
plt.xlabel("Male Smokers (%)")
plt.ylabel("Life Expectancy")
plt.grid(True)
plt.tight_layout()
plt.show()

# 3️⃣ Pie chart: COVID case distribution
plt.figure(figsize=(6, 6))
covid_df['continent'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, shadow=True)
plt.title("COVID Case Distribution by Continent")
plt.ylabel("")
plt.tight_layout()
plt.show()
