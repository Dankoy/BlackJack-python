 
import bs4, requests

res = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.95147000000003&lon=-91.76930999999996')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, features="html5lib")
#print(noStarchSoup)


weather = noStarchSoup.select('div #current_conditions_detail')
print(weather[0].getText())
