from bs4 import BeautifulSoup as bs
import requests as rqs
import csv

file = open('CSVfiles/newBooks.csv', 'w')
writeCSV = csv.writer(file)
headerurl = 'https://www.amazon.in/gp/bestsellers/books/1318158031/ref=zg_bs_nav_books_1'

#writeCSV.writerow(['Action & Adventure', 'Arts, Film & Photography', "Biographies, Diaries & True Accounts", "Business & Economics","Children's & Young Adult", "Comics & Mangas","Computing, Internet & Digital Media","Crafts, Home & Lifestyle", "Crime, Thriller & Mystery","Engineering", "Exam Preparation","Fantasy, Horror & Science Fiction" ])

header = rqs.get(headerurl)
headerSoup = bs(header.content,'html.parser')
Headers = headerSoup.find_all('div', attrs={"class":"_p13n-zg-nav-tree-all_style_zg-browse-item__1rdKf _p13n-zg-nav-tree-all_style_zg-browse-height-large__1z5B8"})
print(len(Headers))

for i in range(1,35):
    writeCSV.writerow([])

#print(next(Headers[5].children).text)

'''
url = ['https://www.amazon.in/gp/bestsellers/books/1318158031/ref=zg_bs_nav_books_1', 'https://www.amazon.in/gp/bestsellers/books/1318052031/ref=zg_bs_nav_books_1_1318158031']

rows = {
    "AA":[],
    "AF":[]
}
for www in url:
    page = rqs.get(www)
    soup = bs(page.content,'html.parser')
    
    imgs = soup.find_all('div', attrs={"class":"a-section a-spacing-mini _cDEzb_noop_3Xbw5"})
    
    if www == url[0]:
        imgs = soup.find_all('div', attrs={"class":"a-section a-spacing-mini _cDEzb_noop_3Xbw5"})
        for image in imgs:
            print(image.img['alt'])
            rows["AA"].append(image.img["alt"])
                
    elif www == url[1]:
        imgs = soup.find_all('div', attrs={"class":"a-section a-spacing-mini _cDEzb_noop_3Xbw5"})
        for image in imgs:
            print(image.img['alt'])
            rows["AF"].append(image.img["alt"])

#print(rows["AA"])
#print(rows["AF"])

for action, films in zip(rows["AA"], rows["AF"]):
    writeCSV.writerow([action, films])
''' 
    
