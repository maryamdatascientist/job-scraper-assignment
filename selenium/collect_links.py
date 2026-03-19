from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

# Setup Chrome
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

print("Opening job site...")
driver.get("https://boards.greenhouse.io/stripe")

# Let page fully load (simple + reliable)
time.sleep(8)

print("Collecting job links...")

jobs = driver.find_elements(By.CSS_SELECTOR, "a[href*='/jobs/']")

links = []
for job in jobs:
    href = job.get_attribute("href")
    if href:
        links.append(href)

# Remove duplicates
links = list(set(links))

# Save to CSV
with open("data/raw/job_links.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["url"])
    for link in links:
        writer.writerow([link])

print(f"Saved {len(links)} job links")

driver.quit()