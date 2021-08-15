import requests
from bs4 import BeautifulSoup

# setting a vari to use the requests library to open and load a pages source code - then adding a header to set user agent as some websites do not like not having a header
r = requests.get("http://www.pyclass.com/example.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

# setting a vari to hold the content of the source code as interactive data - this is in a single string currently
c = r.content

#  create a new vari to parse the content, and specify what is is parseing as  
soup = BeautifulSoup(c,"html.parser")

#  to have python print out the page is 'readable' html there is a method in BS called .prettify 
# print(soup.prettify())
#  generally you will want to use inspect on a webpage for a much more readable form anyway 

#  createing a new vari to hold all data we want to look for - in the example site used above - looking for all div's with the class city 
#  you can be as specific or broad as is needed
#  if you looking for just one .find will return just the first one
all = soup.find_all("div",{"class":"cities"})

# to extract the specific words we are after here we need to .find_all again - 
# It is important to specify the index of the vari so BS treats it as a single object as it will error if passed an array
# Then we can use the .text on the results - remember to specify the index! 
print(all[0].find_all("h2")[0].text) #this will just return 'London'


# Iterate through the entire list and return all the words in the h2 tags 
for item in all:
    print(item.find_all("h2")[0].text)
    print(item.find_all("p")[0].text)