import pandas as pd
import numpy as np
from datetime import datetime

# Create a sample Netflix dataset
data = {
    'show_id': ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10'],
    'type': ['Movie', 'TV Show', 'Movie', 'TV Show', 'Movie',
             'Movie', 'TV Show', np.nan, 'Movie', 'TV Show'],
    'title': ['The Old Guard', 'Money Heist', 'Extraction', 'Dark', 'The Irishman',
              'Marriage Story', 'Stranger Things', 'The Witcher', None, 'The Crown'],
    'director': ['Gina Prince-Bythewood', 'Álex Pina', 'Sam Hargrave', 'Baran bo Odar',
                 'Martin Scorsese', 'Noah Baumbach', 'The Duffer Brothers',
                 np.nan, 'Francis Lee', 'Peter Morgan'],
    'cast': ['Charlize Theron, KiKi Layne', 'Úrsula Corberó, Álvaro Morte',
             'Chris Hemsworth, Rudhraksh Jaiswal', 'Louis Hofmann, Oliver Masucci',
             'Robert De Niro, Al Pacino', 'Scarlett Johansson, Adam Driver',
             'Millie Bobby Brown, Finn Wolfhard', 'Henry Cavill, Freya Allan',
             np.nan, 'Olivia Colman, Tobias Menzies'],
    'country': ['United States', 'Spain', None, 'Germany',
                'United States, Italy', 'United States',
                'United States', 'United States, Poland', 'United Kingdom', None],
    'date_added': ['2020-07-10', '2019-07-19', '2020-04-24', '2019-06-21',
                   '2019-11-27', '2019-12-06', '2016-07-15',
                   '2019-12-20', None, '2019-11-08'],
    'release_year': [2020, 2017, 2020, 2017, 2019, 2019, 2016, 2019, 2017, 2016],
    'rating': ['R', 'TV-MA', 'R', 'TV-MA', 'R', 'R', 'TV-14', 'TV-MA', None, 'TV-MA'],
    'duration': ['126 min', '4 Seasons', '117 min', '3 Seasons', '209 min',
                 '137 min', '3 Seasons', '2 Seasons', '118 min', '4 Seasons'],
    'listed_in': ['Action, Adventure', 'Crime, Drama', 'Action, Thriller',
                  'Crime, Drama, Mystery', 'Crime, Drama', 'Drama, Romance',
                  'Drama, Fantasy, Horror', 'Action, Adventure, Fantasy',
                  'Drama, Romance', 'Drama, History']
}

# Create DataFrame
netflix_df = pd.DataFrame(data)
print("Original DataFrame:")
print(netflix_df.head())
print("\nShape:", netflix_df.shape)
