import pandas as pd
import os

def clean_job_data(input_path="data/raw/remoteok_jobs.csv", output_path="data/processed/clean_jobs.csv"):
    df = pd.read_csv(input_path)

    # Basic cleaning
    df['title'] = df['title'].str.strip().str.title()
    df['company'] = df['company'].str.strip()
    df['location'] = df['location'].fillna("Remote").str.title()
    df.drop_duplicates(inplace=True)

    # Save cleaned version
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to {output_path}")
    return df

if __name__ == "__main__":
    clean_job_data()
