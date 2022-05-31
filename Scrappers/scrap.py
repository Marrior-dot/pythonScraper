from bs4 import BeautifulSoup as Bs
import csv
import requests as rqs

url = 'https://realpython.github.io/fake-jobs/'
page = rqs.get(url)
file = open("titulo_subtitulo.csv", "w")
writeInFile = csv.writer(file)

writeInFile.writerow(["Títulos", "Subtitulos"])

soup = Bs(page.content,"html.parser")
idContent = soup.find("div",id='ResultsContainer')
titulos = soup.find_all("h2", attrs={"class":"title is-5"})
subtitulos = soup.find_all("h3", attrs={"class":"subtitle is-6 company"})

for title, subtitle in zip(titulos, subtitulos):
    #print("Título: {} / Subtítulo: {}".format(title.text,subtitle.text))
    writeInFile.writerow([title.text, subtitle.text])
    
file.close()
#print(jobs)


#jobs = soup.find_all("div", class_="") 


