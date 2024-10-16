"""
Elisabeth Kollrack
Scheduling Conflict Program
Takes input about which class they tutor for and which times they are scheduled for
and checks for scheduling conflicts
"""


import csv

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
Inputs: Decimal time
Outputs: The time in hh:mm format
Effects: Converts decimal time back to normal time format
"""
def reverse_time_conversion(decimal_time):
    hours = int(decimal_time)
    minutes = int((decimal_time - hours) * 60)
    return f"{hours:02}:{minutes:02}"


# TODO
# input the lecture schedules into the program via CSV file,
# input validation


if __name__ == "__main__":
    lecture_schedule = [(13,15),(3,5)]

    # lecture_choice = input(f"Which class would you like to check for conflicts? ")
    user_input = input("Enter your tutoring times in the format hh:mm - hh:mm, hh:mm - hh:mm:\nex: 13:00-14:00, 09:45-11:30\n")
    tutoring_schedule = convert_tutoring_times(user_input)




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
