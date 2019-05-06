# Downloading images from c.xkcd.com and puts it in ./images folder. 
# Takes integer argument as number of images to download
 
import sys, os, bs4, requests, logging, shutil

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s- %(message)s')

url = "https://c.xkcd.com/random/comic/"
try:
    count = int(sys.argv[1])
except ValueError:
    print('You have to input integer like 1 or 2')
    sys.exit()
    

for j in range(count):
    print('Collecting data... Iteration ' + str(j + 1))
    resp = requests.get(url)
    resp.raise_for_status()

    soup = bs4.BeautifulSoup(resp.text, features="html5lib")
    extrUrl = soup.find_all('img')
    imgLink = ''
    
    for i in extrUrl:
        #logging.debug('Link ' + i.get('src'))
        if 'comics' in i.get('src'):
            imgLink = i.get('src')
            imgLink = imgLink.strip('//')
            logging.debug('Link ' + i.get('src'))
            imgName = imgLink.split('/')
            logging.debug('Image name: ' + imgName[2])
            print('Downloading ./images/' + imgName[2])
            downloadResp = requests.get('http://' + imgLink, stream = True)
            with open('images/' + imgName[2], 'wb') as out_file:
                shutil.copyfileobj(downloadResp.raw, out_file)
            del downloadResp

