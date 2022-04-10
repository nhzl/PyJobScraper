from bs4 import BeautifulSoup
import requests
from csv import writer

search_term = input("Enter search term: ")
location_term = input("Enter location: ")

url = 'https://www.indeed.com/jobs?as_and=' + search_term + '&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l=' + location_term + '%2C%20NE&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=ae9008d2f6729286'

page = requests.get(url).text

soup = BeautifulSoup(page, 'lxml')
job = soup.find('div', class_='slider_item')

company_name = job.find('span', class_='companyName').text.replace(' ','')
location = job.find('div', class_='companyLocation').text
title = job.find('h2', class_='jobTitle').text
urgent = job.find('div', class_='urgentlyHiring')

job_total = [company_name, location, title, urgent]

if urgent == 'None':
    urgent = 'No'
else:
    urgent = 'Yes'


print(f'''
Company Name: {company_name}
Location: {location}
Job Title: {title}
Urgently Hiring: {urgent}
''')

save_option = input("Save Results to .CSV file?(Y/N):").lower()

if save_option == 'n':
    with open("records.csv", "a", newline='') as csv_file:
        csv_reader = writer(csv_file)
        csv_reader.writerow(job_total)
        csv_file.close()
elif save_option == 'n':
    print("Thanks for using the most basic web scraper one can make!")
else:
    print("I will add error handling tomorrow")