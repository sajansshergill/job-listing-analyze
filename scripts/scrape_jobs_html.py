from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

def scrape_jobs_html():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://remoteok.com/remote-data-jobs")
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    job_elements = soup.select("tr.job")
    jobs = []

    for job in job_elements:
        try:
            title = job.select_one("td.position h2").text.strip()
            company = job.select_one("td.company h3").text.strip()
            location = job.get("data-region", "Remote")

            # FIXED: Extract tags safely
            tags = [tag.text.strip() for tag in job.select("div.tags h3")]
            desc_url = "https://remoteok.com" + job.get("data-url", "")

            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "tags": ", ".join(tags),
                "description_url": desc_url
            })
        except Exception:
            continue

    return pd.DataFrame(jobs)

if __name__ == "__main__":
    df = scrape_jobs_html()
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/remoteok_jobs_html.csv", index=False)
    print(f"✅ Saved {len(df)} jobs to data/raw/remoteok_jobs_html.csv")
