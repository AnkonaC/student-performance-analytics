import numpy as np


def calculate_total(row):
    marks = [row["Python"], row["Math"], row["Computer_Networks"]]
    return np.sum(marks)


def calculate_average(row):
    marks = [row["Python"], row["Math"], row["Computer_Networks"]]
    return np.mean(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_pass_fail(row):
    marks = [row["Python"], row["Math"], row["Computer_Networks"]]

    if min(marks) >= 40 and row["Attendance"] >= 75:
        return "Pass"
    else:
        return "Fail"


def get_top_students(data, number=3):
    return data.nlargest(number, "Average")