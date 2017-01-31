import urllib2
from bs4 import BeautifulSoup
import pandas as pd

hdr = {'Accept': 'text/html,application/xhtml+xml,*/*',"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"}
url = 'http://www.wine-searcher.com/biz/all/usa?s=26'


req=urllib2.Request(url,headers=hdr)
#Here I get the error with and without using the header or going html = urllib2.urlopen(url).read()
html = urllib2.urlopen(req).read()
soup=BeautifulSoup(html)

names = []
links = []
addresses = []

for tag in soup.find_all( "tr", { "class" : "wlrwdt" } ):
    for sub_tag in tag.find_all( "td", { "class" : "wlrwdt wlbdrl vtop" } ):
        for sub_sub_tag in tag.find_all( "a", ):
            links.append(sub_sub_tag["href"])
            names.append(' '.join(sub_sub_tag.findAll(text=True)))
    
for tag in soup.find_all( "tr", { "class" : "wlrwdt" } ): 
    mas = tag.find_all( "td", { "class" : "wlrwdt vtop" } )
    if (len(mas) > 0):
        line = ' '.join(mas[1].findAll(text=True))
        line = line.replace("\n", "")
        addresses.append(line)
print addresses




Dict = { 'Name' : names, 'Link' : links, 'Address' : addresses}  
df = pd.DataFrame(Dict, columns = ['Link', 'Name', 'Address'])
#df = pd.DataFrame.from_dict(Dict)


df.to_csv('new2.csv', sep='\t')

print df.head()


