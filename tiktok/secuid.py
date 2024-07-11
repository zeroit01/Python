import requests
from bs4 import BeautifulSoup
import json

username=""
url = "https://www.tiktok.com/@"+username
response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})
soup = BeautifulSoup(response.text, "html.parser")
script_tag = soup.find('script',id='__UNIVERSAL_DATA_FOR_REHYDRATION__')
jzon=json.loads(script_tag.text)['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']['user']

id=jzon['id']
uniqueId=jzon['uniqueId']
nickname=jzon['nickname']
avatarLarger=jzon['avatarLarger']
region=jzon['region']
nickNameModifyTime=jzon['nickNameModifyTime']
uniqueIdModifyTime=jzon['uniqueIdModifyTime']
roomId=jzon['roomId']
secUid=jzon['secUid']
print(secUid)

