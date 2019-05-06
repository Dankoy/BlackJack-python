 
import requests, os

res = requests.get('https://automatetheboringstuff.com/chapter')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

print(res.status_code)

openFile = open('./dd', 'w')
openFile.write(res.text)
openFile.close()
#print(res.text)
