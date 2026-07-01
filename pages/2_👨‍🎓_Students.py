import streamlit as st

st.title("👨‍🎓 Students")




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
