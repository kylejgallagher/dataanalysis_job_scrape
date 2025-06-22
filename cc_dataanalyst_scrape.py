from operator import index

import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas.core.indexes.base import ensure_index

all_salaries = []

# just for salaries
# def scrape():
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
#     }
#
#     for x in range(1, 11):
#         url = f'https://www.careercross.com/en/job-search/result/75170496?page={x}'
#         response = requests.get(url, headers=headers)
#
#         if response.status_code != 200:
#             print(f"Failed to retrieve page {x}")
#             continue
#
#         soup = BeautifulSoup(response.text, 'html.parser')
#         job_boxes = soup.find_all('div', class_='result-job-box')
#
#         for box in job_boxes:
#             rows = box.find_all('tr')
#             for row in rows:
#                 label_td = row.find('td', class_='border job-box-flex')
#                 value_td = row.find('td', class_='job-box-text')
#
#                 if label_td and value_td and 'Salary' in label_td.text:
#                     salary_text = value_td.get_text(strip=True)
#                     all_salaries.append(salary_text)
#
#     # Output
#     for s in all_salaries:
#         print(s)

job_listings = []

def scrape():
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

            job_listings.append({'title': title, 'salary': salary})

    # Output
    # for job in job_listings:
    #     print(f"Title: {job['title']}\nSalary: {job['salary']}\n")


scrape()

df = pd.DataFrame(job_listings)
# print(df)

df.to_csv('careercross_datajobs.csv', index=False, encoding='utf-8-sig')
