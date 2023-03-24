import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com"

#Get HTML
r = requests.get(url)

htmlcontent = r.content

#parse HTML

soup = BeautifulSoup(htmlcontent, 'html.parser')

#print(soup.prettify())

#HTML Tree trasversal

#get title of html page
title = soup.title

#print(title)


#Commonly used type of object
#print(type(title)) #1. Tag
#print(type(title.string)) #2. Naviagble string
#print(type(soup)) #3. BeautifulSoup object

#4. Comment

#Get all the paragraphs from the page

paras = soup.find_all('p')
#print(paras)

#Get all anchors

anchors = soup.find_all('a')
#print(anchors)


#find first para
first_para = soup.find('p')
#print(first_para)

#find classes in first para
class_lst = soup.find('p')['class']
#print(class_lst)

#find all element with class lead
class_darkgray = soup.find('p',class_ ="dark:text-gray-400")
#print(class_darkgray)

#get text from all tags/soup
txt = soup.find('p').get_text()
#print(txt)

#get all text
all_txt = soup.get_text()
#print(all_txt)

#get all the links form anchor tags
all_links = set()
for link in anchors:
    if link.get('href')!='#':
        lnk = url + link.get('href')
        all_links.add(lnk)
        print(lnk)
    

