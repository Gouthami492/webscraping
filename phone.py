import urllib.request
from re import findall

url =" http://www.summet.com/dmsi/html/codesamples/addresses.html"

response = urllib.request.urlopen(url)

html = response.read()

string = html.decode()

phones = findall("\(\d{3}\) \d{3}-\d{4}", string)

for phone in phones:
    print(phone)
