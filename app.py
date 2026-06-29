import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(
    page_title="Tech Learning Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.sidebar.image(
    "assets/logo.png",
    width=300
)

st.sidebar.title("Code & Calm")

st.sidebar.caption("Tech Learning Platform")

st.sidebar.markdown("---")
@st.cache_data
def load_data():
    return pd.read_csv("students_500000.csv")
df = load_data()
with st.sidebar.expander("🎯 Dashboard Filters"):

    course = st.selectbox(
        "📚 Select Course",
        ["All"] + list(df["Course"].unique())
    )

    trainer = st.selectbox(
        "👨‍🏫 Select Trainer",
        ["All"] + list(df["Trainer"].unique())
    )

    status = st.selectbox(
        "📌 Select Status",
        ["All"] + list(df["Status"].unique())
    )

if course != "All":
        df = df[df["Course"] == course]

if trainer != "All":
    df = df[df["Trainer"] == trainer]

if status != "All":
    df = df[df["Status"] == status]

st.title("🎓 Tech Learning Dashboard")

st.caption("📊 Student Enrollment Analytics Dashboard")

st.markdown("---")

tab1, tab2, tab3 = st.tabs([
    "📊 Dashboard",
    "📈 Analytics",
    "👨‍🎓 Students"
])

# ================= Dashboard =================

with tab1:

    today = datetime.now()

    st.write(
        f"📅 Today : {today.strftime('%d %B %Y %I:%M:%S %p')}"
    )

    st.success("👋 Welcome to Code and Calm Dashboard")

    total_students = len(df)
    total_courses = df["Course"].nunique()
    revenue = df["Fees"].sum()
    total_trainers = df["Trainer"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("👨‍🎓 Students", total_students)
    col2.metric("📚 Courses", total_courses)
    col3.metric("👨‍🏫 Trainers", total_trainers)
    col4.metric("💰 Revenue", f"₹{revenue:,}")

# ================= Analytics =================

with tab2:

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

# ================= Students =================

with tab3:

    st.subheader("📋 Student Details")

    search = st.text_input("🔍 Search Course")

    filtered_df = df

    if search:
        filtered_df = filtered_df[
            filtered_df["Course"].str.contains(search, case=False)
            |
            filtered_df["Trainer"].str.contains(search, case=False)
            |
            filtered_df["Status"].str.contains(search, case=False)
        ]

    st.dataframe(filtered_df)