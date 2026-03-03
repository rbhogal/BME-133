from datetime import datetime


"""
Edge case
--------- 

If it's 2027 and joining_year = 2026
but current_month < 8 it means they're a freshman still not a junior

2027 - 2026 = 1 -> 'Sophomore" Not TRUE. They're still freshman. Subtract 1 from years_completed
"""

# If else version
# ---------------


def get_student_class(joining_year):

    current_year = datetime.now().year
    current_month = datetime.now().month

    # Check month
    if current_month < 8:
        current_year = current_year - 1

    years_completed = current_year - joining_year

    # if current year is
    if years_completed == 0:
        return "Freshman"
    elif years_completed == 1:
        return "Sophomore"
    elif years_completed == 2:
        return "Junior"
    elif years_completed == 3:
        return "Senior"
    else:
        return "Super Senior"


print(get_student_class(2025))
print(get_student_class(2024))
print(get_student_class(2023))
print(get_student_class(2022))
print(get_student_class(2021))


# Lookup table version
# --------------------
# def get_student_class(joining_year):

#     current_year = datetime.now().year
#     current_month = datetime.now().month
#     class_names = ['Freshman', 'Sophomore', 'Junior', 'Senior']

#     # Check month
#     if current_month < 8:
#         current_year = current_year - 1


#     years_completed = current_year - joining_year

#     if years_completed < 0:
#         return "Not enrolled"
#     if years_completed >= len(class_names):
#         return "Super Senior"
#     return class_names[years_completed]

# print(get_student_class(2025))
# print(get_student_class(2024))
# print(get_student_class(2023))
# print(get_student_class(2022))
# print(get_student_class(2021))
