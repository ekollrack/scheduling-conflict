
"""
Elisabeth Kollrack
Scheduling Conflict Program for TC
"""

import pandas as pd

df = pd.read_csv('/Users/elisabethkollrack/Tutoring/enrollment_f24.csv')


filtered_selected_df = df.loc[(df[' Subj'] == 'CHEM') & (df['#'] == '1400') & (df['Lec Lab'] == 'LEC'), [' Subj', '#', 'Title', 'Sec', 'Start Time', 'End Time']]


def check_conflict(tutor_schedule, lecture_schedule):
    conflicts = []
    for tutor_slot in tutor_schedule:
        tutor_start, tutor_end = tutor_slot
        for lecture_slot in lecture_schedule:
            lecture_start, lecture_end = lecture_slot
            if tutor_start < lecture_end and lecture_start < tutor_end:
                conflicts.append((tutor_slot, lecture_slot))
    return conflicts

# Test schedules
tutor_schedule = [(8, 9), (12, 13)]
lecture_schedule = [(8, 10), (12,14),(15,16)]


has_conflict = check_conflict(tutor_schedule, lecture_schedule)
if has_conflict:
    for tutor_slot, lecture_slot in has_conflict:
        print(f"Scheduling conflict detected between tutor slot {tutor_slot} and lecture slot {lecture_slot}")
else:
    print("No scheduling conflict.")


