import urllib2
from bs4 import BeautifulSoup

url = "http://indianexpress.com/"

#connecting with urllib2 and syncingup with beautifulsoup
requester = urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
connector = urllib2.urlopen(requester)
connector_reader = connector.read()
soup = BeautifulSoup(connector_reader, "lxml")

Indian_express_headlines = soup.findAll("div", {"class": "other-article"})

# print Indian_express_headlines

# for headlines in Indian_express_headlines:
# 	print headlines

INDIANEXPRESS_HEADLINES_LIST = []

for div in Indian_express_headlines:
    content = div.find('h3').find('a').contents[0]
    INDIANEXPRESS_HEADLINES_LIST.append(content)

# print INDIANEXPRESS_HEADLINES_LIST

for headline in INDIANEXPRESS_HEADLINES_LIST:
    print headline    

