#!/usr/python
from bs4 import BeautifulSoup
from urllib.request import  urlopen

def scrap():
    #Enter the url
    page_link ="https://www.loc.gov/rr/print/list/057_chron.html"
    # To open the url
    page_response = urlopen(page_link)
    #print (page_response)
    #To get the conntent from the web page
    page_content =BeautifulSoup(page_response,'html.parser')
    print  (page_content)

    check = page_content.find_all('div',attrs={'class':'mw-parser-output'})
    textContent = []

    try:
        page_response = requests.get(page_link, timeout=5)
        if page_response.status_code == 200:
            print ("connect")
        else:
            print(page_response.status_code)
            # notify, try again
    except requests.Timeout as e:
        print("It is time to timeout")
        #print(str(e))

    """for i in range(0, 20):
    paragraphs = page_content.find_all("p")[i].text
    textContent.append(paragraphs)# to add the data to variable
paragraphs = page_content.find_all("p")[i].text
#To get the date by using bueatiful soup below methpds
#soup.title
#soup.title.string
#soup.a
#soup.p
#soup.select('p')
#soup.find_all('p')
# i[id] 
#soup.p['class]
#soup.find['p']
#soup.find_all['div',attrs={'class':'class_name'}]
#soup.find['table',{'class':'class_name'}]
#soup.find_all('a')
#soup.find(id="link3")
#soup.find(i)
#soup.find_all(class_='classname')

"""

scrap()





