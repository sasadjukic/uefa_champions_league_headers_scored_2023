
import pandas as pd 
from pathlib import Path

data = pd.read_excel('crosses_headers_scored_champions_league.xlsx')

# get clubs with more than 150 crosses attempted
selected = data[data['crosses_attempted'] > 150]

# select categories to display
clubs = selected[['club', 'crosses_attempted', 'crosses_completed', 'crossing_accuracy', 'attempted_crosses_per_match', 'headers_scored']] 

# sort the table with the most headers scored at the top 
clubs.sort_values(['headers_scored'], ascending = 0)