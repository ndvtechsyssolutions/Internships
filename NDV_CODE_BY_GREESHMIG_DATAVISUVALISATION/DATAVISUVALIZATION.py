import pandas as pd
import numpy as np
from datetime import datetime

# Create a sample IPL dataset
data = {
    'match_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'season': ['2023', '2023', '2023', '2023', '2023', 
               '2022', '2022', '2022', '2022', np.nan],
    'city': ['Mumbai', 'Delhi', 'Bangalore', 'Ahmedabad', 'Kolkata',
             'Chennai', 'Hyderabad', 'Jaipur', 'Pune', None],
    'date': ['2023-04-09', '2023-04-10', '2023-04-12', '2023-04-14', '2023-04-16',
             '2022-05-01', '2022-05-03', '2022-05-05', '2022-05-07', '2022-05-09'],
    'team1': ['MI', 'DC', 'RCB', 'GT', 'KKR',
              'CSK', 'SRH', 'RR', 'PBKS', 'LSG'],
    'team2': ['CSK', 'RR', 'KKR', 'LSG', 'SRH',
              'MI', 'RCB', 'DC', 'GT', 'PBKS'],
    'toss_winner': ['MI', 'RR', 'RCB', 'GT', 'KKR',
                    'CSK', 'SRH', 'RR', 'PBKS', 'LSG'],
    'toss_decision': ['field', 'bat', 'field', 'bat', 'field',
                      'bat', 'field', 'bat', 'field', np.nan],
    'result': ['normal', 'normal', 'normal', 'tie', 'normal',
               'normal', 'normal', 'no result', 'normal', 'normal'],
    'dl_applied': [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    'winner': ['MI', 'RR', 'RCB', 'GT', 'KKR',
               'CSK', 'SRH', None, 'PBKS', 'LSG'],
    'win_by_runs': [15, 25, 0, 0, 18, 7, 0, np.nan, 12, 5],
    'win_by_wickets': [0, 0, 8, 0, 0, 0, 9, np.nan, 0, 0],
    'player_of_match': ['Rohit Sharma', 'Jos Buttler', 'Virat Kohli', 'Hardik Pandya',
                        'Andre Russell', 'Ruturaj Gaikwad', 'Kane Williamson',
                        None, 'Liam Livingstone', 'KL Rahul'],
    'venue': ['Wankhede Stadium', 'Arun Jaitley Stadium', 'M. Chinnaswamy Stadium',
              'Narendra Modi Stadium', 'Eden Gardens', 'M. A. Chidambaram Stadium',
              'Rajiv Gandhi Stadium', 'Sawai Mansingh Stadium', 'MCA Stadium', None],
    'umpire1': ['Nitin Menon', 'Anil Chaudhary', 'K. N. Ananthapadmanabhan',
                'C. K. Nandan', 'Virender Sharma', 'Nitin Menon', 'Anil Chaudhary',
                'K. N. Ananthapadmanabhan', 'C. K. Nandan', None],
    'umpire2': [None, 'Bruce Oxenford', 'Paul Reiffel', 'Marais Erasmus',
                'Richard Illingworth', 'Bruce Oxenford', 'Paul Reiffel',
                'Marais Erasmus', 'Richard Illingworth', None],
    'umpire3': ['Shamshuddin', None, 'Yeshwant Barde', 'Krishna Hariharan',
                'Pashchim Pathak', 'Shamshuddin', None, 'Yeshwant Barde',
                'Krishna Hariharan', None]
}

# Convert to DataFrame
ipl_df = pd.DataFrame(data)

# Show first few rows
print(ipl_df.head())
