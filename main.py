from bs4 import BeautifulSoup
import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Cookie": "session-id=136-3547298-1682643; session-id-time=2082787201l; csm-hit=tb:TDJZKRZFRPVC417N42Q5+sa-3M93R1XAKD51J95YY8AF-9SYXW0HHC4MZM2PA0W5P|1727567801448&t:1727567801448&adb:adblk_no; ad-oo=0; ci=e30; ubid-main=135-1309134-5172517; session-token=bNGUPrt7UrUV2vUeVgsCf6VMdkIIS/0IM/do13mElFwkIGiXPxo6TCV03b+/OITsG0cZdE5x34ftUZONiS85Zos89BtQlbCpKrwobYKCYemaqHhZfZVNSLUtdxtfuoLZmKlsejT4tW55i+IegaN/o7uFLDNHTHvoQpfwQ6c2M1L9EYse4jXYegD+DRmQV5jWhdZAON+nHr9NGgpqdDKWdj4jXHIVzOzVSmzFFqzxxjgw20WCgqIUWpO9YkX0Qc3VbrIexgbhxX6nZT0ECLMwESNsyJt5N+R6wikk6PTlvozb0duLWJdwTkQpIA5ac/47GeRzV4jY1y/louVOKohEbnkv+7BHuM9b",
    "Host": "www.imdb.com",
    "Priority": "u=0, i",
    "Referer": "https://www.imdb.com/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"
}

base_url = 'https://www.imdb.com/search/title/'
parameters = {
    'title': 'comedy'
}
response = requests.get(base_url, params=parameters, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

select_1 ='.ipc-metadata-list-summary-item'

elements = soup.select(select_1)
select_2 = '.ipc-title__text'

for element in elements:
    result = element.select(select_2)
    print(result[0].text)