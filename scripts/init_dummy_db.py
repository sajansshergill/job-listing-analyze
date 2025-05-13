import sqlite3
import pandas as pd
import os

# Ensure the data folder exists
os.makedirs("data", exist_ok=True)

# Dummy job data
dummy_data = pd.DataFrame({
    "title": ["Data Scientist", "ML Engineer", "AI Researcher", "Data Analyst", "BI Developer"],
    "company": ["TechCorp", "InnoSoft", "DeepAI", "Insights LLC", "VizTech"],
    "location": ["Remote", "New York", "San Francisco", "Remote", "Austin"],
    "description": [
        "Python, SQL, ML skills needed.",
        "TensorFlow, PyTorch experience required.",
        "Deep learning and NLP expertise.",
        "Dashboarding and analysis.",
        "Power BI and data warehouse skills."
    ]
})

# Save to local SQLite DB
conn = sqlite3.connect("data/job_listings.db")
dummy_data.to_sql("jobs", conn, if_exists="replace", index=False)
conn.close()

print("✅ Dummy job database created at: data/job_listings.db")
