import os 
import csv

csvData = [['Rank','Company','Location','Year end','Salesrise','sales','Staff','Comment']]
file = open('SCRP1.csv', 'a')
writer = csv.writer(file)
writer.writerows(csvData)
file.close()

"""csvData = [['1','Spi-global','Adyar','2019','70%','3.5M','1500','verygoodplace'],['1','Spi-global','Adyar','2019','70%','3.5M','1500','verygoodplace'],['1','Spi-global','Adyar','2019','70%','3.5M','1500','verygoodplace']]
for i in  csvData:
    with open('SCRP1.csv', 'a') as csvFile:
         writer = csv.writer(csvFile)
         writer.writerows(csvData)
    csvFile.close()


csvData = [['Rank','Company','Location','Year end','Salesrise','sales','Staff','Comment']]
with open('SCRP1.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
	
import csv
csvData = [['Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]
with open('person.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()"""