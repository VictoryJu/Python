import bs4
from bs4 import BeautifulSoup
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')

soup = BeautifulSoup(html.text, 'html.parser')
data1 = soup.find('div', {'class':'weather_box'})

pprint(soup)

find_address = data1.find('span', {'class':'btn_select'}).text
print('현재 위치: '+find_address)

find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
print('현재 온도:'+find_currenttemp+'도')

data2 = data1.findAll('dd')

find_dust = data2[0].find('span', {'class':'num'}).text
find_ultra_dust = data2[1].find('span', {'class':'num'}).text
find_ozone = data2[2].find('span', {'class':'num'}).text

print('현재 미세먼지: '+find_dust)
print('현재 초미세먼지: '+find_ultra_dust)
print('현재 오존지수: '+find_ozone)

mask = find_dust[0:2]

if int(mask) <= 30:
    print("현재 미세먼지 적정")
elif int(mask) <= 80:
    print("현재 미세먼지 보통")
elif int(mask) <= 150:
    print("현재 미세먼지 나쁨")
elif int(mask) >= 151:
    print("현재 미세먼지 최악")