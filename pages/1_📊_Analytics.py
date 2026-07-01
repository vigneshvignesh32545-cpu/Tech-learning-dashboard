import streamlit as st

st.title("📊 Analytics")

course_count = df["Course"].value_counts().reset_index()
course_count.columns = ["Course", "Students"]

fig = px.bar(
        course_count,
        x="Course",
        y="Students",
        title="Students by Course"
    )

st.plotly_chart(fig, use_container_width=True)

fig2 = px.pie(
        course_count,
        names="Course",
        values="Students",
        title="Course Popularity"
    )

st.plotly_chart(fig2, use_container_width=True)

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