import requests, pandas
from bs4 import BeautifulSoup

# setting the .get to recieve the html of the webpage we are looking to scrape and then setting the content to a vari

r = requests.get("https://www.rightmove.co.uk/property-for-sale/Datchet.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
#print(c)
# as this print is just horrid and unreadable - we using the built in parser and prettify to make it readable

soup = BeautifulSoup(c,"html.parser")
#print(soup.prettify())

# the next bit comes down to understanding how the webpage is built and what elements we are looking to interact with 
# using the inspect element in the webpage is easier to view this then using the .prettify method above
# we are looking for class and element tags to narrow down what we need

all = soup.find_all("div",{"class":"l-searchResult is-list"})
#print(all)

# as each item we have in our array only has 1 price, we can filter out the specific tage we need and use.text to remove all the tags and leave just the text
# as the resust is a str we can use built in string methods with this - so have used .replace to remove the spaces with nothing to make it a much cleaner result
all[0].find("div",{"class":"propertyCard-priceValue"}).text.replace(" ","")

# loop through every element in the all vari and get the prices/ address / whatever info we want using the same as above 
#using .strip() to remove trailing whitespace for the address and title so we do not get a funky output with squashed words etc 

for item in all:
    print(item.find("address",{"class":"propertyCard-address"}).text.strip())
    print(item.find("h2",{"class":"propertyCard-title"}).text.strip())
    print(item.find("div",{"class":"propertyCard-priceValue"}).text.replace(" ",""))
    print(item.find("div",{"class":"propertyCard-branchSummary"}).find("span").text)
    print(" ")

# if you get a result with type None then use try/ except to get around it - below is example pretending there is a None type 

# for item in all:
#     print(item.find("address",{"class":"propertyCard-address"}).text.strip())
#     print(item.find("h2",{"class":"propertyCard-title"}).text.strip())
#     try:
#         print(item.find("div",{"class":"propertyCard-priceValue"}).text.replace(" ",""))
#     except:
#         pass
#     print(" ")

# if there are multipule text items inside the tag you are looking for then you can use the .find inside the method to further drill down - example 
#     print(item.find("h2",{"class":"propertyCard-title"}).find("secondInsideTag").text) as we have in the loop above for class":"propertyCard-branchSummary

# to make this a useable format, we are going to add this into a python dict and use this to create a list of value pairs to export to CSV

# we create a new empty list so to pass to pandas in the next function
# we then loop through each item and add a new keypair to the dict inside the loop and then append this results to the the list so at the end of the entire loop we will have a list with every matching key pairs to pass to pandas
list = []
for item in all:
    d={}
    d["Address"] = item.find("address",{"class":"propertyCard-address"}).text.strip()
    d["Bedrooms"] = item.find("h2",{"class":"propertyCard-title"}).text.strip()
    d["Price"] = item.find("div",{"class":"propertyCard-priceValue"}).text.replace(" ","")
    d["Activity"] = item.find("div",{"class":"propertyCard-branchSummary"}).find("span").text
    list.append(d)

# we create the data frame, ready to be exported
df = pandas.DataFrame(list)

# outputting the dataframe as a table, using an addittional encoding so the currency displays correctly 
df.to_csv("test_output_scrape.csv",encoding='utf-8-sig')



###############################################################################################################################################
# the above is only the first page, all below is to extend this to the next pages 
###############################################################################################################################################

# after looking for what the 'rule' was for the page urls changing we can create the base page and user a new loop to iterate through the links
# for rightmove the '&index=24&' is what changes for the page listings - 0-23 is the first 24 listings on page one, 24 to 48 would be page 2 and so on (the example I used only has 2 pages)

# using range 0,30, step of 24 to iterate through each link and we can use this to get our list

import requests, pandas
from bs4 import BeautifulSoup

r = requests.get("https://www.rightmove.co.uk/property-for-sale/Datchet.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
c
soup = BeautifulSoup(c,"html.parser")
all = soup.find_all("div",{"class":"l-searchResult is-list"})
all[0].find("div",{"class":"propertyCard-priceValue"}).text.replace(" ","")


# we have moved the origional for loop inside this new for loop, so we loop through all the urls and then in each one, loop through and pull the data
list = []
base = "https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E7959&index=24&propertyTypes=&mustHave=&dontShow=&furnishTypes=&keywords="
for page in range (0,30,24):
    print(base.replace("&index=24","&index="+str(page))+".html")
    r = requests.get(base.replace("&index=24","&index="+str(page))+".html")
    c = r.content
    soup = BeautifulSoup(c,"html.parser")
    all = soup.find_all("div",{"class":"l-searchResult is-list"})
    for item in all:
        d={}
        d["Address"] = item.find("address",{"class":"propertyCard-address"}).text.strip()
        d["Bedrooms"] = item.find("h2",{"class":"propertyCard-title"}).text.strip()
        d["Price"] = item.find("div",{"class":"propertyCard-priceValue"}).text.replace(" ","")
        d["Activity"] = item.find("div",{"class":"propertyCard-branchSummary"}).find("span").text
        list.append(d)

df = pandas.DataFrame(list)
df.to_csv("full_output_scrape.csv",encoding='utf-8-sig')