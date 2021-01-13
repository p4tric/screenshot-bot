import urllib.parse
import urllib.request

url = 'https://222.com'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name': 'Deez Nuts'}
headers = {'User-Agent': user_agent}

data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, {}, headers)
response = urllib.request.urlopen(req)
the_page = response.read()


lists = ["https://www.111.com", "https://222.com", "https://www.333.com/"]

"""
for link in lists:
    print(link)
    urllib.request.urlopen(link)
"""
