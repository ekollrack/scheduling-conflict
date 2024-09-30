
"""
Elisabeth Kollrack
Scheduling Conflict Program for TC
"""

import pandas as pd

df = pd.read_csv('/Users/elisabethkollrack/Tutoring/enrollment_f24.csv')


filtered_selected_df = df.loc[(df[' Subj'] == 'CHEM') & (df['#'] == '1400') & (df['Lec Lab'] == 'LEC'), [' Subj', '#', 'Title', 'Sec', 'Start Time', 'End Time']]

print(filtered_selected_df)
