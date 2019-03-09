#!/usr/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from  urllib.request import  urlopen
import csv

urlpage =  'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
page = urlopen(urlpage)

soup = BeautifulSoup(page,'lxml')

title1    = soup.title

tile_data = title1.string



right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
results =right_table.find_all('tr')
#print (results)

rows   = [['NO','state(or)unionteratory','acapitalcity','legistativecapital','judicialcapital','year','fcapital']]

file   = open('states&capitals.csv','w')
wirter = csv.writer(file)
wirter.writerows(rows)
file.close()
for result in results:
    data = result.find_all('th')
    if len(data) == 0:
       continue
	
    data1 = result.find_all('a')
	
    if len(data1) == 0:
       continue
    #print (data)
    data2 = result.find_all('td')
    if len(data2) == 0:
       continue
    #print (data)
	
    serial  =  data[0].get_text()
    state   = data1[0].get_text()
    capital = data2[0].get_text()
    lcapital= data2[1].get_text()
    jcapital= data2[2].get_text()
    year    = data2[3].get_text()
    fcapital= data2[4].get_text()
    print ("Sno: ",serial)
    print ("State(or)unionteratory: ",state)
    print ("capitacity: ",capital)
    print ("legistativecapital: ",lcapital)
    print ("judicialcapital: ",jcapital)
    print ("year: ",year)
    print ("odl-capitalcity: ",fcapital)
	setdata=[[serial],[state],[capital],[lcapital],[jcapital],[year],[fcapital]
    file   = open('states&capitals.csv','w')
    wirter = csv.writer(file)
    wirter.writerows(rows)
    file.close()
   
"""

#now print the first link


#x = soup.find_all('a')

#for i in x:
#    y = i.get('href')
#now we are finding the list of tables
	
#all_tables=soup.find_all('table')
word = [['No']]
file = open('test.csv','w')
write = csv.writer(file)
write.writerows(word)
file.close()
for i in range(1,101):
    s = [[i]]
    file = open('test.csv','a')
    write = csv.writer(file)
    write.writerows(s)
    file.close()
#print (data)
    
#print (right_table)

#print (all_tables)	 
	

#get the heading 2


#head2 = soup.h2

#print (head2)
#results = table.find_all('a')
#results = table.find_all('a')

#print (soup)

#onlydata = head.get_text()
#onlydata =head.get_text()

#print ("heading:",onlydata)


#<h1 id="firstHeading" class="firstHeading" lang="en">List of state and union territory capitals in India</h1>
#//*[@id="bodyContent"]

#head= soup.h1


#print ("the tile is: ",tile_data)


"""

