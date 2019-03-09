#!/usr/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from  urllib import  urlopen
import csv

urlpage =  'http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'

page = urlopen(urlpage)

soup = BeautifulSoup(page, 'html.parser')

#print soup

# find results within table
table = soup.find('table', attrs={'class': 'tableSorter'})
results = table.find_all('tr')





#print('Number of results', len(results))
rows = []
rows.append(['Rank', 'Company Name', 'Webpage', 'Description', 'Location', 'Year end', 'Annual sales rise over 3 years', 'Sales £000s', 'Staff', 'Comments'])
#print(rows)

for result in results:
    # find all columns per result
    data = result.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
    # write columns to variables
    rank = data[0].getText()
    company = data[1].getText()
    location = data[2].getText()
    yearend = data[3].getText()
    salesrise = data[4].getText()
    sales = data[5].getText()
    staff = data[6].getText()
    comments = data[7].getText()
    #print('Company is', company)
    #print('The company ranks is',rank)
    #companyname = data[1].find('span', attrs={'class':'company-name'}).getText()
    #print companyname
    if rank == '100':
       ran  = data[0].get_text()
       cmp  = data[1].find('span', attrs={'class':'company-name'}).get_text()
       loc  = data[2].get_text()
       year = data[3].get_text()
       
       sal  = data[5].get_text()
       staf = data[6].get_text()
       cmnt = data[7].get_text()
	   
	   #display the data 
	   print "Company name: ",cmp
	   print "lccation:",loc
	   print "year",year
	   print "sale information",salesrise
	   print "staff information",staf
	   print "comment",cmnt
	   print ('\n')
	   
	   
	   
	output = [[rank,cmp,location,year,salesrise,sales,staff,comments]]
    with open('SCRP1.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
       

       
-- INSERT --
