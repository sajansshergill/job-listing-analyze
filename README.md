# AI-Enhanced Job Listings Analyzer

## 📌 Objective
Develop an ethical web scraping pipeline that extracts remote job listings from public job boards, cleans and stores the data in structured formats, and uses AI tools to extract insights like required skills. The final output includes dashboards showing skill trends by job title, company, or location.

## Overview
A project that scrapes job boards, cleans and stores data, and uses AI to extract skill trends from job descriptions.

## Features
- Ethical scraping with Selenium
- AI summarization of job requirements
- Structured SQL/CSV storage
- Visual dashboards for skill analysis

## Technologies Used
Python, Selenium, BeautifulSoup, Firecrawl/OpenAI, SQL, Matplotlib, Git

## How to Run
1. Clone repo
2. Install requirements (`pip install -r requirements.txt`)
3. Update config.py
4. Run scripts in order

## Ethical Notes
- Fully respects robots.txt
- Scrapes only publicly available, non-authenticated pages

## 📁 Folder Structure
job_listings_analyzer/
│
├── data/                      # Raw and processed data files
│   ├── raw/                  
│   └── processed/             
│
├── notebooks/                 # Jupyter notebooks for exploration and visualization
│   └── job_trends_analysis.ipynb
│
├── scripts/                   # Python scripts for modular functionality
│   ├── scrape_jobs.py
│   ├── clean_data.py
│   ├── summarize_jobs.py
│   └── store_data.py
│
├── visuals/                   # Saved charts and plots
│
├── requirements.txt           # Project dependencies
├── .gitignore                 
├── README.md                  
└── config.py                  # Configurable variables (URLs, delay, selectors, etc.)


## 🧠 Core Technologies & Libraries
- Python, Selenium, BeautifulSoup

- pandas, re, time, json

- Seaborn, Matplotlib

- Firecrawl or OpenAI API for job summarization

- SQLite or PostgreSQL for structured storage

- Git for version contro

