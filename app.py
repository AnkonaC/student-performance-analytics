
import pandas as pd
import streamlit as st
from functions import (
    calculate_total,
    calculate_average,
    calculate_grade,
    check_pass_fail,
    get_top_students,
)

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Student Performance Analytics System")
st.write("Analyze student marks, grades, attendance, and class performance.")

data = pd.read_csv("students.csv")

data["Total"] = data.apply(calculate_total, axis=1)
data["Average"] = data.apply(calculate_average, axis=1)
data["Grade"] = data["Average"].apply(calculate_grade)
data["Result"] = data.apply(check_pass_fail, axis=1)

col1, col2, col3 = st.columns(3)
col1.metric("Total Students", len(data))
col2.metric("Class Average", f"{data['Average'].mean():.2f}")
col3.metric(
    "Pass Rate",
    f"{(data['Result'] == 'Pass').mean() * 100:.1f}%"
)

st.subheader("Student Results")
st.dataframe(data, use_container_width=True)

st.subheader("Class Analysis")
highest = data.loc[data["Average"].idxmax()]
lowest = data.loc[data["Average"].idxmin()]

col1, col2, col3 = st.columns(3)
col1.metric("Highest Average", f"{highest['Average']:.2f}", str(highest["Name"]))
col2.metric("Lowest Average", f"{lowest['Average']:.2f}", str(lowest["Name"]))
col3.metric("Failed Students", int((data["Result"] == "Fail").sum()))

st.subheader("Subject-wise Averages")
subjects = ["Python", "Math", "Computer_Networks"]

subject_averages = pd.DataFrame({
    "Subject": subjects,
    "Average": [data[subject].mean() for subject in subjects],
})

st.bar_chart(subject_averages.set_index("Subject"))

best_subject = max(subjects, key=lambda subject: data[subject].mean())
st.write(f"**Best-performing subject:** {best_subject}")

st.subheader("Top 3 Students")
top_students = get_top_students(data)
st.dataframe(
    top_students[["Name", "Average", "Grade"]],
    use_container_width=True,
)

st.caption(
    "Pass rule: at least 40 marks in every subject and attendance of at least 75%."
)
