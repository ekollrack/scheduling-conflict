"""
Elisabeth Kollrack
Tutoring Center
Schedule Conflict Checker
"""

import pandas as pd

# Mapping day abbreviations to full names
day_mapping = {
    'M': 'Monday',
    'T': 'Tuesday',
    'W': 'Wednesday',
    'R': 'Thursday',
    'F': 'Friday'
}

def time_conversion(time, am_pm=None):
    """
    Converts time from 'HH:MM' format to total minutes from midnight.

    Parameters:
        time (str): The time in 'HH:MM' format.
        am_pm (str, optional): 'AM' or 'PM' for 12-hour format conversion.

    Returns:
        int: Total minutes from midnight.
    """
    h, m = map(int, time.split(':'))

    if am_pm:  # Convert 12-hour format to 24-hour
        if am_pm.lower() == 'pm' and h != 12:
            h += 12
        elif am_pm.lower() == 'am' and h == 12:
            h = 0  # Midnight

    return h * 60 + m

def reverse_time_conversion(total_minutes):
    """
    Converts total minutes from midnight back to 'HH:MM AM/PM' format.

    Parameters:
        total_minutes (int): The total minutes from midnight.

    Returns:
        str: The time in 'HH:MM AM/PM' format.
    """
    hours = total_minutes // 60
    minutes = total_minutes % 60

    am_pm = "AM" if hours < 12 else "PM"
    if hours == 0:
        hours = 12
    elif hours > 12:
        hours -= 12

    return f"{hours:02}:{minutes:02} {am_pm}"

def convert_tutoring_times(times):
    """
    Converts a string of tutoring time slots into tuples of start and end times in minutes.

    Parameters:
        times (str): A string of tutoring times formatted as 'hh:mm AM/PM-hh:mm AM/PM'.

    Returns:
        list: A list of tuples, each containing start and end times in minutes.
    """
    tutoring_times = []
    for t in times.split(','):
        start, end = t.split('-')
        start_time, am_pm_start = start.strip().rsplit(' ', 1)
        end_time, am_pm_end = end.strip().rsplit(' ', 1)

        start_minutes = time_conversion(start_time, am_pm_start)
        end_minutes = time_conversion(end_time, am_pm_end)

        tutoring_times.append((start_minutes, end_minutes))
    return tutoring_times

def lectures_data_frame(name, number, day):
    """
    Extracts the lecture schedule for a specific course and day from a CSV file.

    Parameters:
        name (str): The course abbreviation (e.g., 'CHEM').
        number (str): The course number (e.g., '1400').
        day (str): The day of the week to check (e.g., 'M' for Monday).

    Returns:
        list: A list of tuples containing start and end times of lectures in minutes.
    """
    df = pd.read_csv('enrollment_f24.csv')
    df = df[[' Subj', '#', 'Start Time', 'End Time', 'Lec Lab', 'Days']]

    # Filter by course abbreviation and number
    filtered = df[(df[' Subj'].str.strip().str.upper() == name) &
                  (df['#'].astype(str).str.strip() == str(number)) &
                  (df['Lec Lab'] == 'LEC')]

    schedule = []
    for _, row in filtered.iterrows():
        if day in row['Days'].strip():  # Ensure spaces are trimmed
            # Convert the start and end times
            start_minutes = time_conversion(row['Start Time'])
            end_minutes = time_conversion(row['End Time'])
            schedule.append((start_minutes, end_minutes))

    return schedule

def check_conflict(tutor, lecture, day):
    """
    Checks for scheduling conflicts between tutoring slots and lecture times.

    Parameters:
        tutor (list): A list of tuples representing tutoring time slots in minutes.
        lecture (list): A list of tuples representing lecture time slots in minutes.
        day (str): The day for which conflicts are checked.
    """
    conflicts = set()
    for tutor_start, tutor_end in tutor:
        for lecture_start, lecture_end in lecture:
            # Check for overlap between tutor and lecture slots
            if tutor_start < lecture_end and lecture_start < tutor_end:
                conflicts.add((tutor_start, tutor_end, lecture_start, lecture_end))

    if conflicts:
        for tutor_start, tutor_end, lecture_start, lecture_end in conflicts:
            print(f"Conflict: Tutor slot {reverse_time_conversion(tutor_start)}-"
                  f"{reverse_time_conversion(tutor_end)} and Lecture slot "
                  f"{reverse_time_conversion(lecture_start)}-"
                  f"{reverse_time_conversion(lecture_end)} on {day_mapping[day]}")
    else:
        print("No scheduling conflict.")

if __name__ == "__main__":
    # User input for tutoring times
    while True:
        tutor_times = input(
            "Enter your tutoring times in the format hh:mm AM/PM-hh:mm AM/PM, "
            "separated by commas for multiple slots:\n"
        )
        # Validate tutoring times format
        try:
            convert_tutoring_times(tutor_times)  # Test conversion
            break  # Exit loop if successful
        except (ValueError, IndexError):
            print("Invalid format. Please make sure your input follows the format 'hh:mm AM/PM-hh:mm AM/PM'.")

    # User input for the day of the tutoring sessions
    while True:
        tutoring_day = input(
            "What day are these times for (only enter 1 day)?\n"
            "Enter 'M' for Monday, 'T' for Tuesday, 'W' for Wednesday, "
            "'R' for Thursday, 'F' for Friday:\n"
        ).strip().upper()

        # Validate day input
        if tutoring_day in day_mapping:
            break
        else:
            print("Invalid input. Please enter 'M', 'T', 'W', 'R', or 'F'.")

    # Convert tutoring times to minutes
    tutoring_schedule = convert_tutoring_times(tutor_times)


    while True:
        class_choice = input("Enter course abbreviation (e.g., 'CHEM'): ").strip().upper()
        class_number = input("Enter course number (e.g., 1400): ").strip()

        # Extract lecture schedule and check for conflicts
        lecture_schedule = lectures_data_frame(class_choice, class_number, tutoring_day)
        print(f"Checking conflicts for {class_choice} {class_number}...")
        check_conflict(tutoring_schedule, lecture_schedule, tutoring_day)

        # Ask if the user wants to check another class
        another_class = input("Would you like to check another class? (yes/no): ").strip().lower()
        if another_class not in ('yes', 'y'):
            break  # Exit loop if user doesn't want to check another class
