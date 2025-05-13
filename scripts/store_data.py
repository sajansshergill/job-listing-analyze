import sqlite3
import pandas as pd
import os

def store_to_db(csv_path="data/processed/gpt_enriched_jobs.csv", db_path="data/job_listings.db"):
    if not os.path.exists(csv_path):
        print(f"❌ CSV not found at {csv_path}")
        return

    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)
    df.to_sql("jobs", conn, if_exists="replace", index=False)
    conn.close()
    print(f"✅ Stored {len(df)} records in {db_path}")

if __name__ == "__main__":
    store_to_db()
