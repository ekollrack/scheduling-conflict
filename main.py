"""
Elisabeth Kollrack
Scheduling Conflict Program
Takes input about which class they tutor for and which times they are scheduled for
and checks for scheduling conflicts
"""


import pandas as pd


"""
Inputs: Tutor and lecture schedules
Outputs: a list of conflicting times
Effects: Checks for overlap between the tutor's schedule and lecture times
"""
def check_conflict(tutor_schedule, lecture_schedule):
    conflicts = []
    for tutor_slot in tutor_schedule:
        tutor_start, tutor_end = tutor_slot
        for lecture_slot in lecture_schedule:
            lecture_start, lecture_end = lecture_slot
            if tutor_start < lecture_end and lecture_start < tutor_end:
                conflicts.append((tutor_slot, lecture_slot))
    return conflicts


"""
Inputs: Time in military time
Outputs: The time in decimal format
Effects: Converts inputted time to a decimal format
"""
def time_conversion(time):
    (h, m) = time.split(':')
    result = int(h) + (int(m) / 60)
    return result


"""
Inputs: List of times the user inputted 
Outputs: The list of times in decimal format
Effects: Converts inputted list of times to a decimal format
"""
def convert_tutoring_times(user_input):
    tutoring_times = []
    converted_tutoring_times = []
    # This for loop formats times as [(time 1: time 2),(time 3: time 4)]
    for t in user_input.split(','):
        start, end = t.split('-')
        tutoring_times.append((start, end))
    # This for loop formats times as [(time 1, time 2),(time 3, time 4)]
    for start, end in tutoring_times:
        converted_start = time_conversion(start)
        converted_end = time_conversion(end)
        converted_tutoring_times.append((converted_start, converted_end))
    return converted_tutoring_times


"""
Inputs: List of lecture times for the specified class
Outputs: The list of times in decimal format
Effects: Converts inputted list of times to a decimal format
"""
def convert_lecture_times(lec_df):
    lecture_schedule = []
    for start, end in lec_df[['Start Time', 'End Time']].values:
        converted_start = time_conversion(start)
        converted_end = time_conversion(end)
        lecture_schedule.append((converted_start, converted_end))
    return lecture_schedule


"""
Inputs: Decimal time
Outputs: The time in hh:mm format
Effects: Converts decimal time back to normal time format
"""
def reverse_time_conversion(decimal_time):
    hours = int(decimal_time)
    minutes = round((decimal_time - hours) * 60)

    # Adds an hour when minutes = 60
    if minutes == 60:
        hours += 1
        minutes = 0
    return f"{hours:02}:{minutes:02}"


"""
Inputs: Class description
Outputs: Data frame of class information
Effects: Creates a data frame from enrollment data
"""
def lectures_data_frame(name,number):
    df = pd.read_csv('enrollment_f24.csv')
    df = df[[' Subj','#','Start Time', 'End Time', 'Lec Lab', 'Days']]
    df = df[(df[' Subj'] == name) &
           (df['Lec Lab'] == 'LEC') &
           (df['Start Time'] != 'Nan') &
           (df['#'] == number)]
    return df

# TODO
# Remove duplicate tuples
# Function for check conflict
# Input validation
# Days of the week

if __name__ == "__main__":

    user_input = input("Enter your tutoring times in the format hh:mm - hh:mm, hh:mm - hh:mm:\nex: 13:00-14:00, 09:45-11:30\n")
    tutoring_schedule = convert_tutoring_times(user_input)
    class_choice = input("Which class would you like to schedule conflicts for? Enter course abbreviation e.g. 'CHEM'\n").upper()
    class_number = input("What is the course number? e.g 1400\n")


    # Finds the class in the enrollment dataset
    lecture_data = lectures_data_frame(class_choice,class_number)
    # Finds the lecture times and adds to lecture schedule
    lecture_schedule = convert_lecture_times(lecture_data)

    # Check for conflicts and print the results
    has_conflict = check_conflict(tutoring_schedule, lecture_schedule)
    if has_conflict:
        for (tutor_start, tutor_end), (lecture_start, lecture_end) in has_conflict:
            print(f"Conflict: Tutor slot {reverse_time_conversion(tutor_start)}-"
                  f"{reverse_time_conversion(tutor_end)} and Lecture slot "
                  f"{reverse_time_conversion(lecture_start)}-"
                  f"{reverse_time_conversion(lecture_end)}")
    else:
        print("No scheduling conflict.")

    print(lecture_schedule)
