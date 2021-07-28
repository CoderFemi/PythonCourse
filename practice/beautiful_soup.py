import requests
from bs4 import BeautifulSoup

uba_url = 'https://www.ubagroup.com/nigeria/help/atm-branch-locator/'
response = requests.get(url=uba_url)
uba_branches = response.text

soup = BeautifulSoup(uba_branches, 'html.parser')
addresses = soup.find_all('td')
addresses_text = [address.getText() for address in addresses]
print(addresses_text)
