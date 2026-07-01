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