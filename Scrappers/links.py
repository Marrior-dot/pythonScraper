from bs4 import BeautifulSoup as bs
import requests as rqs
import csv

file = open('CSVfiles/newBooks.csv', 'w')
writeCSV = csv.writer(file)

writeCSV.writerow(['Action & Adventure', 'Arts, Film & Photography'])

url = ['https://www.amazon.in/gp/bestsellers/books/1318158031/ref=zg_bs_nav_books_1', 'https://www.amazon.in/gp/bestsellers/books/1318052031/ref=zg_bs_nav_books_1_1318158031']
for www in url:
    page = rqs.get(www)
    soup = bs('html.parser', page.content)
    
    if www == url[0]:
        soup.find_all
    
    
