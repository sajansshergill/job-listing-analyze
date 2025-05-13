import streamlit as st
import pandas as pd
import sqlite3
import os

st.set_page_config(page_title="AI-Enhanced Job Listings", layout="wide")
st.title("📊 AI-Enhanced Remote Job Listings Dashboard")

@st.cache_data
def load_data():
    db_path = "data/job_listings.db"
    if not os.path.exists(db_path):
        st.error("❌ job_listings.db not found. Run the scripts first.")
        return pd.DataFrame()

    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM jobs", conn)
    conn.close()
    return df

df = load_data()

if not df.empty:
    st.success(f"✅ Loaded {len(df)} job listings")

    with st.expander("📋 View Job Listings"):
        st.dataframe(df)

    st.subheader("🏢 Top Companies")
    st.bar_chart(df["company"].value_counts().head(10))

    if "tags" in df.columns and df["tags"].notna().any():
        st.subheader("🏷️ Most Common Tags")
        tag_counts = df["tags"].dropna().str.split(', ').explode().value_counts().head(10)
        st.bar_chart(tag_counts)
    else:
        st.info("No tag data available.")

    if "extracted_skills" in df.columns and df["extracted_skills"].notna().any():
        st.subheader("🧠 Top Skills Extracted by GPT")
        skill_counts = df["extracted_skills"].dropna().str.replace("\n", ", ") \
            .str.split(', ').explode().value_counts().head(10)
        st.bar_chart(skill_counts)

        with st.expander("🔍 View Extracted Skills"):
            st.dataframe(df[["title", "company", "extracted_skills"]])
    else:
        st.warning("⚠️ No extracted skills found. Did you run summarize_jobs.py?")
else:
    st.warning("⚠️ No data to display.")
