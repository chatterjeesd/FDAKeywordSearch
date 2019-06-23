from bs4 import BeautifulSoup
import urllib.request
import datetime

keyword= input("Enter ONE Keyword:")
startdatei=input("Enter Start Date (MMDDYYYY):")
enddatei=input("Enter End Date (MMDDYYYY):")



#Program Starta here:-

startdate=datetime.datetime.strptime(startdatei, '%m%d%Y').timestamp()
enddate=datetime.datetime.strptime(enddatei, '%m%d%Y').timestamp()
print('\n',"Searching FDA Database..."'\n')
keywordlist=[]


#This is where all the urls in the downloaded webpage will be appended
urllinks=[]

#Open the downloaded webpage
fo=open("warningletter.html", 'r')

# Soupify the source code and find all url links contained in the source code:
soup = BeautifulSoup(fo, "lxml")
for a in soup.find_all('a', href=True):
    	urllinks.append(a['href'])

for lines in urllinks:
	if 'warning-letters' in lines:
		try:
			dated=str(lines.split('/')[5].split('-')[-1])
			if enddate>=datetime.datetime.strptime(dated, '%m%d%Y').timestamp() >=startdate:
				with urllib.request.urlopen(lines) as url:
					s= url.read().decode('utf-8').lower()
					if keyword in s:
						companysplit=lines.split('/')[5].split('-')[:-2]
						company=str(' '.join(companysplit))
						keywordlist.append(1)
						print("Company: ",company,", Warning Letter Dated (MMDDYYYY):",dated)
					#else:
						#print("Not found")
		except Exception as e:
			print(e)
			continue
print("End of search")
print("Total number of appearances of ",keyword,"is: ",len(keywordlist))

