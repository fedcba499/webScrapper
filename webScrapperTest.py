
from bs4 import BeautifulSoup

import os.path

# from tkfile
# import urllib2
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import re

html_page = urllib2.urlopen("http://legacy.lib.utexas.edu/maps/ams/india/")
soup = BeautifulSoup(html_page)


for link in soup.findAll('a'):

    print (link.get('href'))

    a= str(link.get('href'))
    p =  a.split('.')
    ext = p[-1]
    q = a.split('/')
    imageName = q[-1]
    if ext == "jpg":

        a= a+'\n'
        file = open("linksForMaps3.txt","a")  
        file.write(a)  
        file.close() #to change file access modes 
        # response = urllib2.urlopen(a)
        # html = response.read()
     
        if os.path.exists(imageName):
            pass
        else:
            urllib2.urlretrieve(a, imageName)
    
