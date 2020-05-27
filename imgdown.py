import requests
from bs4 import BeautifulSoup

query = input("search query:")

url = "https://www.google.com/search?hl=en&tbm=isch&sxsrf=ALeKk00__SjccBkbryt3EYFSBkZaRbm_jA%3A1590587635751&source=hp&biw=702&bih=604&ei=83DOXsvAK7GFmgfy1Zu4CQ&q="

r = requests.get(url).content
soup = BeautifulSoup(r, 'lxml')
images = soup.find_all('img')

for image in images:
    src = image.get('src')
    name = src.split(':')[-1]

    img_res = requests.get(src).content

    file = open(name + '.jpg', 'wb')
    file.write(img_res)
    print('Image Download : {}'.format(name))
