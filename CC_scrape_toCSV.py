from operator import index

import requests
from bs4 import BeautifulSoup
import pandas as pd

doda = 'https://doda.jp/DodaFront/View/JobSearchList/j_oc__020602S/-preBtn__3/?page=1'

all_salaries = []


job_listings_dataanalyst = []
job_listings_python = []

def scrape_data_analyst():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    for x in range(1, 11):
        url = f'https://www.careercross.com/en/job-search/result/75170496?page={x}'
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to retrieve page {x}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        job_boxes = soup.find_all('div', class_='result-job-box')

        for box in job_boxes:
            # Get job title
            title_tag = box.find('a', class_='job-details-url')
            title = title_tag.get_text(strip=True) if title_tag else "No title found"

            # Initialize salary
            salary = "Not listed"

            # Loop through <tr> elements to find salary
            rows = box.find_all('tr')
            for row in rows:
                label_td = row.find('td', class_='border job-box-flex')
                value_td = row.find('td', class_='job-box-text')

                if label_td and value_td and 'Salary' in label_td.text:
                    salary = value_td.get_text(strip=True)
                    break  # Stop after finding salary

            # -----------

            job_listings_dataanalyst.append({'title': title, 'salary': salary})

    # Output
    for job in job_listings_dataanalyst:
        print(f"Title: {job['title']}\nSalary: {job['salary']}\n")





def scrape_python():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    for x in range(1, 19):
        url = f'https://www.careercross.com/en/job-search/result/75171209?page={x}'
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to retrieve page {x}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        job_boxes = soup.find_all('div', class_='result-job-box')

        for box in job_boxes:
            # Get job title
            title_tag = box.find('a', class_='job-details-url')
            title = title_tag.get_text(strip=True) if title_tag else "No title found"

            # Initialize salary
            salary = "Not listed"

            # Loop through <tr> elements to find salary
            rows = box.find_all('tr')
            for row in rows:
                label_td = row.find('td', class_='border job-box-flex')
                value_td = row.find('td', class_='job-box-text')

                if label_td and value_td and 'Salary' in label_td.text:
                    salary = value_td.get_text(strip=True)
                    break  # Stop after finding salary

            # -----------

            job_listings_python.append({'title': title, 'salary': salary})

    # Output
    for job in job_listings_python:
        print(f"Title: {job['title']}\nSalary: {job['salary']}\n")

scrape_data_analyst()
scrape_python()
#
df_da = pd.DataFrame(job_listings_dataanalyst)
df_py = pd.DataFrame(job_listings_python)

with open('CareerCross Job Scrape.csv', 'w') as f:
    df_da.to_csv(f, index=False)
    f.write('\n')
    df_py.to_csv(f, index=False)
