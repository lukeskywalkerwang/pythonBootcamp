from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://230fifthave.com/directory/')
soup = BeautifulSoup(response, 'html.parser')
atag = soup.find_all(class_="showroom-title")

print(soup.title.text)

companyDir = {}
urllist = []
companyName = []
for tag in atag:
    urllist.append(tag.get('href'))
    companyName.append(tag.get('title').replace('View ', ''))

# print("\n".join(urllist))
# print("\nCompany Name")
# print("\n".join(companyName))

for i in range(len(urllist)):
    response = urlopen(urllist[i])
    soup = BeautifulSoup(response, 'html.parser')
    ctag = str(soup.find_all(class_='company-name-text'))
    phoneNum = ctag[ctag.find("Phone") + 8: ctag.find("Fax:") - 20]
    email = ctag[ctag.find("Email") + 7: ctag.find("Website") - 14]
    print(companyName[i], phoneNum, email)
    companyDir[companyName[i]] = [phoneNum, email]

print(companyDir)
