import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/students.csv")

st.title("🎓 Tech Learning Dashboard")

# KPI Cards
total_students = len(df)
total_courses = df["Course"].nunique()
revenue = df["Fees"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Students", total_students)
col2.metric("Courses", total_courses)
col3.metric("Revenue", f"₹{revenue:,}")

# Course-wise Students
course_count = df["Course"].value_counts().reset_index()
course_count.columns = ["Course", "Students"]

fig = px.bar(
    course_count,
    x="Course",
    y="Students",
    title="Students by Course"
)

st.plotly_chart(fig, use_container_width=True)

# Course Popularity
fig2 = px.pie(
    course_count,
    names="Course",
    values="Students",
    title="Course Popularity"
)

st.plotly_chart(fig2, use_container_width=True)

# Student Status
status_count = df["Status"].value_counts().reset_index()
status_count.columns = ["Status", "Count"]

fig3 = px.pie(
    status_count,
    names="Status",
    values="Count",
    hole=0.5,
    title="Student Status"
)

st.plotly_chart(fig3, use_container_width=True)

st.dataframe(df)