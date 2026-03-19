# Job Scraper Assignment

## Overview

This project implements an end-to-end job scraping pipeline using *Selenium* and *Scrapy* to collect, extract, and analyze job listings. The extracted data is stored in CSV format and visualized through a simple web interface.

---

## Tech Stack

* Python
* Selenium
* Scrapy
* Pandas
* Matplotlib
* HTML/CSS

---

## Features

* Selenium for collecting job links
* Scrapy for extracting structured job data
* Data storage in CSV format
* Data analysis using Pandas
* Visualization using Matplotlib
* Simple frontend interface for displaying results

---

## Project Structure


job-scraper-assignment/
│
├── analysis/        # Data analysis scripts
├── data/            # Raw and processed data
│   ├── raw/
│   └── processed/
├── docs/            # Frontend + report
├── job_scraper/     # Scrapy project
├── selenium/        # Selenium scripts
├── README.md
├── .gitignore


---

## Data Sources

### Primary Source (Used for Scraping)
- https://realpython.github.io/fake-jobs/

This dataset was used as the main source because:
- It provides structured job listings
- It is publicly accessible
- It avoids legal and anti-scraping restrictions

### Referenced Real-World Platforms (Not Scraped)
- https://www.indeed.com/
- https://www.linkedin.com/jobs/
- https://www.glassdoor.com/

These platforms were analyzed conceptually to understand:
- Real-world job trends
- Common job fields and requirements

*Note:* These platforms were not scraped due to dynamic content and anti-bot protections.

## How to Run

### 1. Install dependencies


pip install -r requirements.txt


### 2. Collect job links (Selenium)


python selenium/collect_links.py


### 3. Run Scrapy spider


cd job_scraper
scrapy crawl jobs -o jobs_scrapy.csv


### 4. Move output file


mv jobs_scrapy.csv ../data/processed/


### 5. Run analysis


cd ../analysis
python analysis.py


### 6. Run frontend


cd ../docs
python -m http.server 8000


Then open:


http://localhost:8000/index.html


---

## Analysis Summary

* Total jobs analyzed: 100
* High demand for software and data-related roles
* Python-related jobs are prominent
* Remote roles are increasingly common
* Hiring is concentrated among a few companies

---

## Version Control

* Development performed on the develop branch
* Final stable code merged into main
* Release tagged as v1.0

---

## Future Improvements

* Scraping real job platforms using APIs
* Handling pagination and dynamic content
* Adding advanced visualizations
* Deploying as a web application

---

## Author

Maryam 
