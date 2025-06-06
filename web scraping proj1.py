pip install requests beautifulsoup4 lxml
import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

job_cards = soup.select(".card-content")
for card in job_cards:
    title = card.select_one("h2.title").text.strip()
    company = card.select_one("h3.company").text.strip()
    location = card.select_one("p.location").text.strip()
    print(f"{title} | {company} | {location}")

import re

for card in job_cards:
    location = card.select_one("p.location").text.strip()
    if re.search(r"New York", location, re.IGNORECASE):
        title = card.select_one("h2.title").text.strip()
        print(f"{title} in {location}")

from lxml import html

tree = html.fromstring(response.text)
titles = tree.xpath('//h2[@class="title"]/text()')
companies = tree.xpath('//h3[@class="company"]/text()')
locations = tree.xpath('//p[@class="location"]/text()')

for title, company, location in zip(titles, companies, locations):
    print(f"{title.strip()} | {company.strip()} | {location.strip()}")

import csv

with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Company", "Location"])
    for card in job_cards:
        title = card.select_one("h2.title").text.strip()
        company = card.select_one("h3.company").text.strip()
        location = card.select_one("p.location").text.strip()
        writer.writerow([title, company, location])

