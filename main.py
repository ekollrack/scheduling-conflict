
"""
Elisabeth Kollrack
Scheduling Conflict Program for TC
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


def time_conversion(time):
    (h, m) = time.split(':')
    result = int(h) + (int(m) / 60)
    return result

time = "09:00"

print(time_conversion(time))


# Test schedules
tutor_schedule = [(8.5, 9.3333), (12, 13)]
lecture_schedule = [(8, 10), (12,14),(15,16)]

tutoring_times = input("Enter your tutoring times in the format hh:mm: ")

has_conflict = check_conflict(tutor_schedule, lecture_schedule)
if has_conflict:
    for tutor_slot, lecture_slot in has_conflict:
        print(f"Scheduling conflict detected between tutor slot {tutor_slot} and lecture slot {lecture_slot}")
else:
    print("No scheduling conflict.")


