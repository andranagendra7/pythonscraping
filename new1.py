
def fib(n):
     a, b = 0, 1
     while a < n:
        print(a, end=' ')
        a, b = b, a+b
     print()
fib(1000)
# """import scrp5
#
# import os
#
# path = 'd:/nagendra/scrap/CompletedArticles.csv'
# file = open(path,'rb')
# def test():
#
#     print(file.read())
#     file.close()
# test()
# #pd = emp('Nagendra','205048','N.NagendraAndra@spi-global.com')
# scrp5.aws(('10'))
# #import os
# # link = urlopen("https://www.usa.gov/federal-agencies/")
# #link = urlopen("https://www.usa.gov/branches-of-government")
# #link = urlopen('file:///D:/Nagendra/python/Browse%20Publications%20-%20Wiley%20Online%20Library.html')
# # link = urlopen('https://www.usa.gov/branches-of-government')
# import platform
#
# x = platform.system()
# print(x)
#
# for i in range(21):
#      #print ("I will respect Every peple")
#      print ("I will feels always Every one is good ")
#     #print ("I'm a Positive thinker")
#     #print('I will chanage')
#     # print ("Every day, i choose  Happy ")
#     #  print ("Every day, i choose  Smile ")
#     #  print ("Every day, i speak   Softly")
#     #  print ("Every day, i learn   Newthings")
#     # print ("Every day, i will make diifference")
#     #print ("Today ,i finish my tasks on time")
#
#
# #practice:
#
# print (heading)
#     #test1 = heading.find('ul')
#     #print (test1.find_all('li'))
#     #for i in heading:
#     #    print (i.find('li'))
#     """#x = soup.find('p',{'class':'intro-text--search'})
#     #print (x.text)
#     y =soup.find('div', attrs={'class':'fea-cntntmddl-img'})
#     z = y.find('img')
#     image = z.get('src')
#     out = image.split('/')
#     print (image)
#     #path= r'D:/Nagendra/scrap'
#     file = open(out[-1],'wb')
#     file.close()
#     #value = [1,2,3]
#
#     # print (soup.h1.text)
#     # result = ((soup.find_all('p')[20:30]))
#     # for i  in result:
#     #     print (i.text)
#     # print (soup.title.get_text())
#     # print (soup.h1.get_text())
#     # page1 = soup.find('ul', {'class': "az-list group"})
#     # pagelist = (page1.find_all('li'))
#     # #for page in pagelist:
#     # #   print('the page name: %s' %page.get_text())
#     # # we get the pages list points
#     # # pagecontent = soup.find('ul', {'class':'one_column_bullet'})
#     # # pagedata= pagecontent.find_all('li')
#     # # for output in pagedata:
#     # #     fdata = (output.find('a'))
#     # #     print (fdata.get('href'))
#     # # #print(pagedata)
#     # conten2= soup.find('div',{'class':'shade dwn'})
#     # subdata=conten2.find('ul')
#     # data = subdata.find_all('li')
#     # for result in data:
#     #     print (result.get_text().strip())
#     # page2 =
#     # for link in page1:
#     #     print(link.get_text())
#     # print (page1)"""
# """
# link = 'https://miningthedetails.com/blog/python/BeautifulSoupWebScraping/'
# #link = 'https://www.wileyindia.com/Wiley_Online_Resources/IIT%20Varanasi/IIT%20Varanasi.html'
#
# #link = 'https://miningthedetails.com/blog/python/BeautifulSoupWebScraping/'
#
# #link ='https://www.kdnuggets.com/2018/02/web-scraping-tutorial-python.html'
#
# #url = 'http://www.arstechnica.com/'
# data = urlopen(link).read()
# soup = BeautifulSoup(data,'lxml')
#
#
# print (soup.find('div', attrs={'class':'entry-content'}))
#
# for i in sam2:
#
#     #print (i.find('td'))
#     text   = i.get('href')
#     #result = text.('href')
#     print (text)
#
#
# x = soup.find_all('div')
#
# print (soup)
#
#
# #x = soup.find_all('p')
# x = soup.find_all('a')
# for i in x:
#     print (i.get('href'))
#
# links = soup.findAll('ul')
# for link in links:
#     var1 = link.get('span')
#     print (var1)
# soup = BeautifulSoup(link,'lxml')
#
#
# print (soup.find(class_='rlist'))
# #print (soup.find_all('a'))
# all_links = soup.find_all("ul")
#
# for link in all_links:
#     d = link.find('li')
#     n = d.find('a')
#     print (n)"""
# """
# journals_list = []
# def scrap():
#     # var1 = soup.find('div', id='alphaFace')
#     var2 = soup.find('div', attrs={'class': 'search-result showPublications'})
#     var3 = var2.find('ul', {'class': 'rlist separator search-result__body titles-results'})
#     # var2 = soup.find('div',attrs={'class':'search-result__meta'})
#
#     # var2 = var1.find('url')
#
#     var4 = var3.find_all('li')
#
#     for journal in var4:
#         # journal_name=journal.find('a')
#         journal_name = journal.find('span', {'class': 'hlFld-Title'})
#         journals_list.append(journal_name.text)
#
#     # print('page1 output:')
#     # print(journals_list)
#
#
# scrap()
# #value =[1,2,3]
#
# link = urlopen('file:///D:/Nagendra/python/Browse%20Publications%20-%20Wiley%20Online%20Library.html')
#
# #link = urlopen('https://www.usa.gov/branches-of-government')
# soup = BeautifulSoup(link,'lxml')
# #print (soup)
# journals_list =[]
#
# def scrap():
#
#     #var1 = soup.find('div', id='alphaFace')
#     var2 = soup.find('div',attrs={'class':'search-result showPublications'})
#     var3 = var2.find('ul',{'class':'rlist separator search-result__body titles-results'})
#     # var2 = soup.find('div',attrs={'class':'search-result__meta'})
#
#     #var2 = var1.find('url')
#
#     var4 = var3.find_all('li')
#
#     for journal in var4:
#         #journal_name=journal.find('a')
#         journal_name  = journal.find('span',{'class':'hlFld-Title'})
#         journals_list.append(journal_name.text)
#
#     #print('page1 output:')
#     #print(journals_list)
#
#
# scrap()
#
# link2 = urlopen('file:///D:/Nagendra/python/Browse%20Publications%20-%20Wiley%20Online%20Library2.html')
# soup = BeautifulSoup(link2,'lxml')
# journals_list2 = []
# def scrap2():
#     # var1 = soup.find('div', id='alphaFace')
#     var2 = soup.find('div', attrs={'class': 'search-result showPublications'})
#     var3 = var2.find('ul', {'class': 'rlist separator search-result__body titles-results'})
#     # var2 = soup.find('div',attrs={'class':'search-result__meta'})
#
#     # var2 = var1.find('url')
#
#
#     var4 = var3.find_all('li')
#
#     for journal in var4:
#         # journal_name=journal.find('a')
#         journal_name = journal.find('span', {'class': 'hlFld-Title'})
#         journals_list2.append(journal_name.text)
#     #print('\npage2 out:')
#     #print(journals_list2)
#
#
# scrap2()
#
# link3 = urlopen('file:///D:/Nagendra/python/Browse%20Publications%20-%20Wiley%20Online%20Library3.html')
# soup = BeautifulSoup(link3,'lxml')
# journals_list3 = []
# def scrap3():
#     # var1 = soup.find('div', id='alphaFace')
#     var2 = soup.find('div', attrs={'class': 'search-result showPublications'})
#     var3 = var2.find('ul', {'class': 'rlist separator search-result__body titles-results'})
#     # var2 = soup.find('div',attrs={'class':'search-result__meta'})
#     # var2 = var1.find('url')
#     var4 = var3.find_all('li')
#
#     for journal in var4:
#         # journal_name=journal.find('a')
#         journal_name = journal.find('span', {'class': 'hlFld-Title'})
#         journals_list3.append(journal_name.text)
#     #print('\npage3 out:')
#     #print(journals_list3)
#
# scrap3()
# total_journals = journals_list+journals_list2+journals_list3
#
# print (total_journals)
#
# link4 = urlopen('https://onlinelibrary.wiley.com/action/showPublications?PubType=journal&pageSize=20&startPage=&alphabetRange=a')
#
# soup = BeautifulSoup(link4,'lxml')
# def scrap4():
#     # var1 = soup.find('div', id='alphaFace')
#     var2 = soup.find('div', attrs={'class': 'search-result showPublications'})
#
#     var3 = var2.find('ul', {'class': 'rlist separator search-result__body titles-results'})
#     # var2 = soup.find('div',attrs={'class':'search-result__meta'})
#
#     # var2 = var1.find('url')
#     journals_list4 = []
#
#     var4 = var3.find_all('li')
#
#     for journal in var4:
#         # journal_name=journal.find('a')
#         journal_name = journal.find('span', {'class': 'hlFld-Title'})
#         journals_list4.append(journal_name.text)
#     print('\npage3 out:')
#     print(journals_list4)
# """
# # scrap4()
#
#
"""for i in range(1,22):
    #print ("I'm a Positive Thinker")
    #print("Geat things will take time")
    #print("Cool mode")
    #print('self learner')
    print('quick learner')
    #print ('Today, i will finish jenkins pipeline') """

def test(b):
    a,n= 0,1
    while (a < b):
        print(a,end=' ')
        a,n=n,a+n
    print(' ')
test(100)


from urllib.request import urlopen
from bs4 import BeautifulSoup


import requests
the_web_page_as_a_string = requests.get(some_path).content

from lxml import html
myTree = html.fromstring(the_web_page_as_a_string)
td_list = [ e for e in myTree.iter() if e.tag == 'td']

"""
journals_list = []
class automation:
    global    journals_list
    def scrap():

        #link = urlopen('file:///D:/Nagendra/python/Browse%20Publications%20-%20Wiley%20Online%20Libraryb.html')

        link=[]
        for i in range(21):
            #value.append(i)
            text = 'https://www.wileyindia.com/government-job-exams?p=' + str(i)
            link.append(text)
        for j in link:
            ulink=urlopen(j)
            soup = BeautifulSoup(ulink, 'lxml')
            print(soup.title.get_text())
            file = open('ouptu.tx', 'w')
            var = soup.find('div', attrs={'class': 'products wrapper list products-list'})
            #print (var)
            var2 = var.find_all('li')
            print('\nAuthors information:')
            for k in var2:
                auth = k.find('div', attrs={'class': 'product details product-item-details'})
                print(auth.find('p').get_text())
            print("Books Details:")
            for m in var2:
               link = m.find_all('a')
               for i in link:
                   result = i.get('href')
                   #print(result)
               for h in link:
                    result2 = h.get_text().strip('Buy Now').strip()
                    print(result2)

        #chk = soup.find(id="maincontent")
        #pgcls = soup.find('div',attrs={'class' : 'pages'})
        #print (chk.find_all('li'))


        print(soup.title.get_text())
        file = open('ouptu.tx','w')
        var  = soup.find('div',attrs={'class':'products wrapper list products-list'})
        #print (var)

        var2 = var.find_all('li')
        #link = j.find_all('a')
        links=[]
        print ("Books Details:")
        for j in var2:
            #print(j)
            link= j.find_all('a')

            for i in link:
                result= i.get('href')
            for h in link:
                result2 = h.get_text().strip('Buy Now').strip()
                print(result2)
        print('\nAuthors information:')
        for k in var2:
             auth = k.find('div', attrs={'class':'product details product-item-details'})
             print(auth.find('p').get_text())
                #get_cls = k.find('div',attrs={'class' :'product details product-item-details'})
        print('\nBooks price information:')
        for l in var2:
            price = l.find('div',attrs={'class' : 'product-price '})
            print(price.get_text().strip())

            #final_out=link.get('href')
            #print(final_out)

        for i in links:
            get_link = (i.get('href'))
            print (get_link)
        file.write((soup.title.get_text()))
        file.close()

        var2 = soup.find('div', attrs={'class': 'search-result showPublications'})
        var3 = var2.find('ul', {'class': 'rlist separator search-result__body titles-results'})
        var4 = var3.find_all('li')
        for journal in var4:
            journal_name = journal.find('span', {'class': 'hlFld-Title'})
            journals_list.append(journal_name.text)
    scrap()
    #print (journals_list)



for i in range(22):

    #print ("Think Positive")
    #print ("Patience is Power ")
    #print(' Today, i choose Peace and Happy ')

    print (" i will do code coverage")
#
# patience
# patient"""