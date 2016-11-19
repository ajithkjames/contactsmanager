from bs4 import BeautifulSoup
import urllib
for i in range(11):
	r = urllib.urlopen('https://ktu.edu.in/eu/afn/affiliationInstitutes.htm?pageNo='+str(i)+'&districtId=&').read()
	soup = BeautifulSoup(r,"html5lib")
	table=soup.find('table')
	span=table.find_all('span', attrs={'class':'span-contact'})
	for email in span[::2]:
	    print email.text



