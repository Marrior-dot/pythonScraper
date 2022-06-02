from bs4 import BeautifulSoup as bs
import pandas as pd
import requests as rqs
import csv

file = open('CSVfiles/newBooks.csv', 'w')
writeCSV = csv.writer(file)

data = {}

headerArray = []
urls = []
headerurl = 'https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_unv_books_1_1318158031_2'
header = rqs.get(headerurl)
headerSoup = bs(header.content,'html.parser')
Headers = headerSoup.find_all('div', attrs={"class":"_p13n-zg-nav-tree-all_style_zg-browse-item__1rdKf _p13n-zg-nav-tree-all_style_zg-browse-height-large__1z5B8"})


#fazer o resto do loop em casa

for i in range(1,35):    
    data[Headers[i].a.text] = ["0"]
        
    
df = pd.DataFrame(data)
print(df)

#for i in range(1,35):
 #   headerArray.append(Headers[i].a.text)
  #  urls.append(Headers[i].a['href'])

#writeCSV.writerow(headerArray)

rows = []
subRows = []


'''
for www in urls:
    page = rqs.get("https://www.amazon.in/"+www)
    soup = bs(page.content,'html.parser')
    
    imgs = soup.find_all('div', attrs={"class":"a-section a-spacing-mini _cDEzb_noop_3Xbw5"})
    
    for image in imgs:
        subRows.append(image.img["alt"])
    rows.append(subRows)

writeCSV.writerow([item for list in rows for item in list])     


    if www == urls[0]:
        imgs = soup.find_all('div', attrs={"class":"a-section a-spacing-mini _cDEzb_noop_3Xbw5"})
        for image in imgs:
           # print(image.img['alt'])
            rows["AA"].append(image.img["alt"])
                
    elif www == urls[1]:
        imgs = soup.find_all('div', attrs={"class":"a-section a-spacing-mini _cDEzb_noop_3Xbw5"})
        for image in imgs:
            #print(image.img['alt'])
            rows["AF"].append(image.img["alt"])
'''
#for action, films in zip(rows["AA"], rows["AF"]):
 #   writeCSV.writerow([action, films])
