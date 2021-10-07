import requests
from bs4 import BeautifulSoup
import lxml
from itertools import zip_longest
import csv

# get the jobs in a csv file
url ="https://www.linkedin.com/jobs/search?keywords=&location=Morocco&locationId=&geoId=102787409&sortBy=R&f_TPR=r86400&position=1&pageNum=0"
result = requests.get("https://www.linkedin.com/jobs/search?keywords=&location=Morocco&locationId=&geoId=102787409&sortBy=R&f_TPR=r86400&position=1&pageNum=0")

src = result.content

soup = BeautifulSoup(src,"lxml")

JobTitles =[]
company=[]
location=[]
posted=[]
info = []


job_title = soup.find_all("h3",{"class":"base-search-card__title"})
company_name = soup.find_all("h4",{"class":"base-search-card__subtitle"})
job_location = soup.find_all("span",{"class":"job-search-card__location"})
time = soup.find_all("time")
more_info=soup.find_all("a", {"class":"base-card__full-link"})
for i in range(len(more_info)):
    JobTitles.append(job_title[i].text.strip())
    company.append(company_name[i].text.strip())
    location.append(job_location[i].text.strip())
    posted.append(time[i].text.strip())
    info.append(more_info[i].attrs['href'])
#create the csv file    
file_list=[JobTitles , company , location , posted ,info ]
exported = zip_longest(*file_list)
with open("C:\mouad\web scrap bs4\linkedin\linkedin_jobstest.csv","w") as myfile:
    we = csv.writer(myfile)
    we.writerow(["job title","company","location","date ","more information"])
    we.writerows(exported)












