import csv
import re
from datetime import datetime


def read_csv(filepath):
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


def clean_data(data):
    cleaned_data = []
    for row in data:
       
        row['title'] = row['title'].strip().title() if row['title'] else 'Unknown'
        row['type'] = row['type'].strip().capitalize() if row['type'] else 'Unknown'
        row['director'] = row['director'].strip() if row['director'] else 'Unknown'
        row['cast'] = row['cast'].strip() if row['cast'] else 'Unknown'
        row['country'] = row['country'].strip() if row['country'] else 'Unknown'
        row['listed_in'] = row['listed_in'].strip() if row['listed_in'] else 'Unknown'
        row['description'] = row['description'].strip().capitalize() if row['description'] else 'Unknown'

        
        if row['date_added']:
            try:
                date_obj = datetime.strptime(row['date_added'].strip(), '%B %d, %Y')
                row['date_added'] = date_obj.strftime('%Y-%m-%d')
            except:
                row['date_added'] = 'Invalid Date'
        else:
            row['date_added'] = 'Unknown'

        
        row['duration'] = re.sub(r'[^\d]', '', row['duration']) if row['duration'] else '0'

        
        row['rating'] = row['rating'].strip() if row['rating'] else 'Unknown'

       
        row['release_year'] = row['release_year'] if row['release_year'] else 'Unknown'

        cleaned_data.append(row)
    return cleaned_data


def print_cleaned_data(data, count=5):
    print(f"\nShowing first {count} cleaned records:\n")
    for i, row in enumerate(data[:count]):
        print(f"Record {i+1}:")
        for key, value in row.items():
            print(f"  {key}: {value}")
        print("-" * 50)


def save_cleaned_data(data, filepath):
    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


input_file = 'netflix_titles.csv'
output_file = 'netflix_titles_cleaned.csv'

raw_data = read_csv(input_file)
cleaned_data = clean_data(raw_data)

print_cleaned_data(cleaned_data)
save_cleaned_data(cleaned_data, output_file)

print(f"\n Cleaned data saved to '{output_file}'")
