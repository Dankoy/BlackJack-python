
import requests, sys, webbrowser, bs4


url = 'https://www.google.com/search?q='
search_str = sys.argv[1:]

print('Googling... ' + url + ' '.join(search_str))
response = requests.get(url + ' '.join(search_str))
response.raise_for_status()
print(response.status_code)
print(response.url)

soup = bs4.BeautifulSoup(response.text, features="html5lib")
#print(soup.prettify())
#links = soup.find_all('div', class_='TbwUpd')
links = soup.select('.r a')
print(links)

#print(response.text)


