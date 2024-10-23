import pandas as pd
# TODO
# change time format
# add multiple classes

day_mapping = {
    'M': 'Monday',
    'T': 'Tuesday',
    'W': 'Wednesday',
    'R': 'Thursday',
    'F': 'Friday'
}


def check_conflict(tutor, lecture, day):
    conflicts = set()
    for tutor_slot in tutor:
        tutor_start, tutor_end = tutor_slot
        for lecture_slot in lecture:
            lecture_start, lecture_end = lecture_slot
            if tutor_start < lecture_end and lecture_start < tutor_end:
                conflicts.add((tutor_slot, lecture_slot))

    if conflicts:
        for (tutor_start, tutor_end), (lecture_start, lecture_end) in conflicts:
            print(f"Conflict: Tutor slot {reverse_time_conversion(tutor_start)}-"
                  f"{reverse_time_conversion(tutor_end)} and Lecture slot "
                  f"{reverse_time_conversion(lecture_start)}-"
                  f"{reverse_time_conversion(lecture_end)} on {day_mapping[day]}")
    else:
        print("No scheduling conflict.")


def time_conversion(time):
    (h, m) = time.split(':')
    result = int(h) + (int(m) / 60)
    return result


def convert_tutoring_times(times):
    tutoring_times = []
    converted_tutoring_times = []
    for t in times.split(','):
        start, end = t.split('-')
        tutoring_times.append((start.strip(), end.strip()))
    for start, end in tutoring_times:
        converted_start = time_conversion(start)
        converted_end = time_conversion(end)
        converted_tutoring_times.append((converted_start, converted_end))
    return converted_tutoring_times


def reverse_time_conversion(decimal_time):
    hours = int(decimal_time)
    minutes = round((decimal_time - hours) * 60)

    if minutes == 60:
        hours += 1
        minutes = 0
    return f"{hours:02}:{minutes:02}"


def lectures_data_frame(name, number, day):
    df = pd.read_csv('enrollment_f24.csv')
    df = df[[' Subj', '#', 'Start Time', 'End Time', 'Lec Lab', 'Days']]

    # Filter by the selected day
    df = df[(df[' Subj'] == name) &
            (df['Lec Lab'] == 'LEC') &
            (df['Start Time'] != 'Nan') &
            (df['#'] == number) &
            (df['Days'].str.contains(day))]

    schedule = []
    for start, end in df[['Start Time', 'End Time']].values:
        converted_start = time_conversion(start)
        converted_end = time_conversion(end)
        schedule.append((converted_start, converted_end))
    return schedule


if __name__ == "__main__":
    tutor_times = input(
        "Enter your tutoring times in the format hh:mm - hh:mm, hh:mm - hh:mm:\nex: 13:00-14:00, 09:45-11:30\n")
    tutor_date = input("What day are these times for (only enter 1 day please)? \n"
                       "Enter 'M' for Monday, 'T' for Tuesday, 'W' for Wednesday, 'R' for Thursday, 'F' for Friday \n")

    while tutor_date not in day_mapping:
        tutor_date = input("Invalid input. Please enter 'M', 'T', 'W', 'R', or 'F': ")

    tutoring_schedule = convert_tutoring_times(tutor_times)

    class_choice = input(
        "Which class would you like to schedule conflicts for? Enter course abbreviation e.g. 'CHEM'\n").upper()
    class_number = input("What is the course number? e.g 1400\n")

    # Finds the lecture times and adds to lecture schedule
    lecture_schedule = lectures_data_frame(class_choice, class_number, tutor_date)

    # Check for conflicts
    check_conflict(tutoring_schedule, lecture_schedule, tutor_date)
