from urllib.request import urlopen
from bs4 import BeautifulSoup

journals_list = []
serial_num = []
class automation:
    global journals_list
    def scrap():
        #link = urlopen('file:///D:/Nagendra/python/Browse%20Publications%20-%20Wiley%20Online%20Libraryb.html')
        link = urlopen('https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India')

        soup = BeautifulSoup(link, 'lxml')

        list1 = soup.find('table',{'class':'wikitable sortable plainrowheaders'})
        list2 = list1.find_all('tr')
        serial_num = []

        for data in list2:
            result = data.find_all('th')
            if len(result) == 0:
                continue
            print (result)
            result2 = data.find_all('a')
            #print (result2)
            result1 = data.find_all('td')
            if len(result1) == 0:
                continue
            #rint(result1)
            y = serial_num.append(result[0].get_text().strip())

            #serial_num.append(result[1].get_text())
            #serial_num.append(result2[1].get_text())


        file = open('output','ab')
        for  i in serial_num:
             file.write(i)
        file.close()

        """
        var2 = soup.find('div', attrs={'class': 'search-result showPublications'})
        var3 = var2.find('ul', {'class': 'rlist separator search-result__body titles-results'})
        var4 = var3.find_all('li')
        for journal in var4:
            journal_name = journal.find('span', {'class': 'hlFld-Title'})
            journals_list.append(journal_name.text)"""
    scrap()
    #print (journals_list)
