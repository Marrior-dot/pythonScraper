from bs4 import BeautifulSoup as Bs
import requests as rqs
import csv 

url = 'https://www.amazon.in/gp/bestsellers/books/1318158031/ref=zg_bs_nav_books_1'
url
page = rqs.get(url)
soup = Bs(page.content, 'html.parser')

file = open("CSVfiles/books.csv", "w")
writeInFile = csv.writer(file)

writeInFile.writerow(["Action & Adventure"])

BestAA = soup.find_all('div', attrs={"class":"a-section a-spacing-mini _cDEzb_noop_3Xbw5"})

for image in BestAA:
    writeInFile.writerow([image.img['alt']])