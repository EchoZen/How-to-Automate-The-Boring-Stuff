import bs4, requests
# BeautifulSoup is a 3rd party mod that lets you parse html
weblink= 'https://www.weather.gov/'
inspectcss= '#topnews > div.body > h1'
res= requests.get(weblink)
res.raise_for_status()
soup= bs4.BeautifulSoup(res.text, 'html.parser')
elems= soup.select(inspectcss) # from the inspect source
print(elems[0].text)
