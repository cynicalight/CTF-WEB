from requests import post
from concurrent.futures import ThreadPoolExecutor

url = 'http://27.25.151.80:45041/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}


def test_char(char):
    files = {
        'upload_file': ('a', char, 'text/plain')
    }
    response = post(url, headers=headers, files=files)
    print(response.text)
    if '拦截' in response.text:
        banned.append(char)
    else:
        passed.append(char)


banned = []
passed = []

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(test_char, [chr(i) for i in range(32, 128)])

    print(f'Banned: {banned}')
    print(f'Passed: {passed}')
