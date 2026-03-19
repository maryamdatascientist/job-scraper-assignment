# Job Scraper Report

# Overview

This project collects job listings using Selenium and Scrapy and displays them on a web interface.

## Tools Used

- Selenium: for collecting job links
- Scrapy: for extracting job data
- HTML + JavaScript: for displaying results

## Data Fields

- Title
- Company
- Location
- Date
- URL

## Assumptions

- The website structure remains consistent
- Missing fields are replaced with "N/A"

## Setup Instructions

1. Install dependencies:
   pip install scrapy selenium pandas matplotlib

2. Run scraper:
   cd job_scraper
   scrapy crawl jobs -o jobs_scrapy.csv

3. Move file:
   mv jobs_scrapy.csv ../data/processed/

4. Start server:
   python -m http.server 8000

5. Open:
   http://localhost:8000/docs/index.html

## Results

- Successfully scraped ~100+ job listings
- Data displayed in table with search functionality
