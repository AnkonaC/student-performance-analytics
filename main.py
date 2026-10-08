import pandas as pd

from functions import (
    calculate_total,
    calculate_average,
    calculate_grade,
    check_pass_fail,
    get_top_students
)


# Load the student dataset
data = pd.read_csv("students.csv")


# Calculate total and average marks
data["Total"] = data.apply(calculate_total, axis=1)
data["Average"] = data.apply(calculate_average, axis=1)


# Assign grades
data["Grade"] = data["Average"].apply(calculate_grade)


# Check pass/fail
data["Result"] = data.apply(check_pass_fail, axis=1)


# Display complete student results
print("\n" + "=" * 70)
print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 70)

print("\nSTUDENT PERFORMANCE:")
print(data.to_string(index=False))


# Overall statistics
class_average = data["Average"].mean()
highest_average = data["Average"].max()
lowest_average = data["Average"].min()

highest_student = data.loc[data["Average"].idxmax(), "Name"]
lowest_student = data.loc[data["Average"].idxmin(), "Name"]

pass_count = (data["Result"] == "Pass").sum()
fail_count = (data["Result"] == "Fail").sum()


print("\n" + "=" * 70)
print("                     CLASS ANALYSIS")
print("=" * 70)

print(f"Overall Class Average : {class_average:.2f}")
print(f"Highest Average       : {highest_average:.2f} ({highest_student})")
print(f"Lowest Average        : {lowest_average:.2f} ({lowest_student})")
print(f"Number of Passed      : {pass_count}")
print(f"Number of Failed      : {fail_count}")


# Subject-wise analysis
subjects = ["Python", "Math", "Computer_Networks"]

print("\n" + "=" * 70)
print("                 SUBJECT-WISE ANALYSIS")
print("=" * 70)

for subject in subjects:
    print(f"{subject} Average: {data[subject].mean():.2f}")


best_subject = max(subjects, key=lambda subject: data[subject].mean())

print(f"\nBest Performing Subject: {best_subject}")


# Top 3 students
top_students = get_top_students(data)

print("\n" + "=" * 70)
print("                    TOP 3 STUDENTS")
print("=" * 70)

for index, student in top_students.iterrows():
    print(
        f"{student['Name']} - "
        f"Average: {student['Average']:.2f} - "
        f"Grade: {student['Grade']}"
    )


print("\n" + "=" * 70)
print("                  ANALYSIS COMPLETE")
print("=" * 70)