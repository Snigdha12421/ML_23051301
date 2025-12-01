# ML_DATA_COLLECTION
This repository contains practice scripts and sample datasets collected through three basic data-gathering methods commonly used in Machine Learning:

✅ 1. Manual Data Entry

File: 01_manual_data.py
Output: manual_data.csv

Demonstrates how to manually create datasets using Python lists/dictionaries.

Useful for building small custom datasets for testing or learning.

✅ 2. API Data Collection

File: 02_api_data.py
Output: swapi_data.csv

Fetches structured data from a public API (example: SWAPI).

Shows how to call APIs, parse JSON, and store results in CSV format.

✅ 3. Web Scraping

File: 03_web_scrap.py
Output: hackernews_latest.csv

Scrapes data from a website (example: Hacker News latest posts).

Demonstrates HTML parsing and extracting information using Python.


🚀 How to Run the Scripts

Clone the repository:

git clone <repo-url>
cd ML_DATA_COLLECTION


Run any of the scripts:

python 01_manual_data.py
python 02_api_data.py
python 03_web_scrap.py


Check the generated CSV files.

📌 Requirements

You may need the following Python packages:

pip install requests beautifulsoup4 pandas
