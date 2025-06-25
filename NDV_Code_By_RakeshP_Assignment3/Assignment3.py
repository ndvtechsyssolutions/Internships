import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'covid_data.csv'
df = pd.read_csv(file_path)





df.fillna({'continents' : "Unknown"}, inplace=True)


df = df.fillna(df.mean(numeric_only=True))


print("Data Set After Preprocessing : \n")
df.describe


print("\nSummary Statistics:")
print(df.describe())
print("Mean:\n", df.mean(numeric_only=True))
print("Median:\n", df.median(numeric_only=True))
print("Count:\n", df.count())


print("\033[1mVISUALIZATIONS\n\n\n\033[0m")



plt.figure(figsize=(8,5))
sns.countplot(x = df['continent'], data = df)
plt.title("Number of Cases In Each Continent")
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sns.lineplot(x = df['male_smokers'], y = df['life_expectancy'])
plt.title("Life Expectency of Male Smokers")
plt.xlabel("Count of Male Smokers")
plt.ylabel("Life Expectency")
plt.grid(True)
plt.tight_layout()
plt.show()

df['continent'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("COVID Case Distribution by Continent")
plt.tight_layout()
plt.show()
