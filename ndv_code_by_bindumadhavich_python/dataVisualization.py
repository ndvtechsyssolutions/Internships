# 📦 Step 1: Install and Import Libraries
!pip install --quiet ipywidgets

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display, clear_output

# 🌐 Step 2: Load Dataset (OWID COVID-19 public data)
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url, parse_dates=['date'])

# Filter out rows with null continents (world aggregates)
df = df[df['continent'].notna()]

# Show columns available
print("Columns in dataset:", df.columns.tolist())

# 🧹 Step 3: Preprocessing
df.columns = df.columns.str.strip().str.lower()
countries = sorted(df['location'].unique())
metrics = ['new_cases', 'new_deaths', 'total_cases', 'total_deaths']
# 🧩 Step 4: Define Interactive Widgets
country_dropdown = widgets.Dropdown(
    options=countries,
    description='Country:',
    value='India'
)

metric_dropdown = widgets.Dropdown(
    options=metrics,
    description='Metric:',
    value='new_cases'
)

chart_radio = widgets.RadioButtons(
    options=['Line Chart', 'Bar Chart', 'Pie Chart'],
    description='Chart:'
)

show_stats = widgets.Checkbox(
    value=True,
    description='Show Summary'
)
# 📊 Step 5: Dashboard Function
def update_dashboard(country, metric, chart_type, show_summary):
    clear_output(wait=True)
    display(country_dropdown, metric_dropdown, chart_radio, show_stats)

    filtered = df[df['location'] == country]

    # Show summary stats
    if show_summary:
        print(f"\n📈 Summary for {country} - {metric}")
        print(f"Mean: {filtered[metric].mean():,.2f}")
        print(f"Median: {filtered[metric].median():,.2f}")
        print(f"Total: {filtered[metric].sum():,.2f}")

    # Plot
    if chart_type == 'Line Chart':
        plt.figure(figsize=(10,5))
        plt.plot(filtered['date'], filtered[metric], label=metric, color='teal')
        plt.title(f"{metric} over time in {country}")
        plt.xlabel("Date")
        plt.ylabel(metric)
        plt.grid(True)
        plt.show()

    elif chart_type == 'Bar Chart':
        monthly = filtered.groupby(filtered['date'].dt.to_period("M"))[metric].sum()
        monthly.index = monthly.index.to_timestamp()
        plt.figure(figsize=(10,5))
        sns.barplot(x=monthly.index, y=monthly.values, color='orange')
        plt.title(f"Monthly {metric} in {country}")
        plt.xticks(rotation=45)
        plt.show()

    elif chart_type == 'Pie Chart':
     latest = filtered[filtered['date'] == filtered['date'].max()]

    if not latest.empty:
        total_cases = latest['total_cases'].values[0]
        total_deaths = latest['total_deaths'].values[0]

        if pd.notna(total_cases) and pd.notna(total_deaths) and (total_cases > 0):
            vals = [total_cases - total_deaths, total_deaths]
            labels = ['Recovered/Active', 'Deaths']

            plt.figure(figsize=(6,6))
            plt.pie(vals, labels=labels, autopct='%1.1f%%', startangle=90)
            plt.title(f"Cases vs Deaths in {country} (Latest)")
            plt.show()
    else:
       print("⚠️ Not enough data to display pie chart.")
# 🧠 Step 6: Display the Dashboard
widgets.interact(
    update_dashboard,
    country=country_dropdown,
    metric=metric_dropdown,
    chart_type=chart_radio,
    show_summary=show_stats
)
