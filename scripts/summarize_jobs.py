import openai
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_jobs_with_gpt(input_csv="data/raw/remoteok_jobs_html.csv", output_csv="data/processed/gpt_enriched_jobs.csv"):
    if not os.path.exists(input_csv):
        print("❌ Input CSV not found.")
        return

    df = pd.read_csv(input_csv)
    if df.empty:
        print("❌ Input CSV is empty.")
        return

    summaries = []

    for i, row in df.iterrows():
        title = str(row.get("title", "")).strip()
        tags = str(row.get("tags", "")).strip()

        if not title:
            summaries.append("None")
            continue

        prompt = f"Extract the top 5 required skills from this job:\nTitle: {title}\nTags: {tags}"
        print(f"\n🔍 Job {i+1}: {title}")

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                timeout=20
            )
            message = response.choices[0].message.content.strip()
            skills = "None" if not message or message.lower() in ["none", "n/a"] else message
            print(f"✅ Extracted: {skills}")
        except Exception as e:
            print(f"❌ GPT Error: {e}")
            skills = "None"

        summaries.append(skills)

    df["extracted_skills"] = summaries
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(output_csv, index=False)
    print(f"\n✅ Saved GPT results to: {output_csv}")

if __name__ == "__main__":
    summarize_jobs_with_gpt()
