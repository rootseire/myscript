import urllib2
from bs4 import BeautifulSoup



for m in range(1, 13):
    for d in range(1, 32):

      if (m == 2 and d > 28):
	break
      elif (m in [4, 6, 9, 11] and d > 30):
	break

      timestamp = '2015' + str(m) + str(d)
      print "Getting data for " + timestamp
      url = "http://www.wunderground.com/history/airport/EICK/2015/" + str(m) + "/" + str(d) + "/DailyHistory.html"
      page = urllib2.urlopen(url)
      soup = BeautifulSoup(page)
      #dayTemp = soup.findAll(attrs={"class":"wx-data"})[8].span.string
      dayTemp = soup.find("span", text="Precipitation").parent.find_next_sibling("td").get_text(strip=True)
      #dayTemp = soup.find(text="Precipitation").next("td").contents[1]
      print dayTemp
      if len(str(m)) < 2:
	mStamp = '0' + str(m)
      else:
	mStamp = str(m)
	
      if len(str(d)) < 2:
	dStamp = '0' + str(d)
      else:
	dStamp = str(d)  
	
      timestamp = '2015' + mStamp + dStamp
      dayTemp = dayTemp.encode('utf-8', 'replace')
      with open('wunder-data.txt', 'a+') as f:
	f.write(timestamp + ',' + dayTemp + '\n')
f.close()