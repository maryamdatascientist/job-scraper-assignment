import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Setup browser
options = Options()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)

# Read links
links = []
with open("data/raw/job_links.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        links.append(row[0])

print(f"Processing {len(links)} jobs...")

data = []

for i, link in enumerate(links):
    try:
        driver.get(link)
        time.sleep(2)

        # ✅ TITLE (robust)
        title = "N/A"
        for tag in ["h1", "h2"]:
            elements = driver.find_elements(By.TAG_NAME, tag)
            for el in elements:
                text = el.text.strip()
                if text and len(text) > 5 and text.lower() != "jobs":
                    title = text
                    break
            if title != "N/A":
                break

        # ✅ LOCATION (basic)
        location = "N/A"
        try:
            location_el = driver.find_element(By.XPATH, "//*[contains(text(),'Location')]")
            location = location_el.text
        except:
            pass

        # ✅ COMPANY (meta tag)
        company = "N/A"
        try:
            company_el = driver.find_element(By.XPATH, "//meta[@property='og:site_name']")
            company = company_el.get_attribute("content")
        except:
            pass

        # ✅ DESCRIPTION (meta tag)
        description = "N/A"
        try:
            desc_el = driver.find_element(By.XPATH, "//meta[@name='description']")
            description = desc_el.get_attribute("content")[:120]
        except:
            pass

        data.append([title, company, location, description, link])
        print(f"{i+1}/{len(links)} → {title}")

    except Exception:
        print(f"Error on {link}")
        continue

driver.quit()

# Save CSV
with open("data/processed/jobs.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "company", "location", "description", "url"])
    writer.writerows(data)

print(f"Saved {len(data)} jobs")