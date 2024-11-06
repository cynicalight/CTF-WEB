import requests
import re

req = requests.session()
url = "http://challenge.basectf.fun:20174/"

answer = 0
while True:
    response = req.post(url , data={"answer": answer})
    print(response.text)
    if "BaseCTF" in response.text:
        print(response.text)
        break
    # 匹配简单的算式
    regex = r" (\d*?)(.)(\d*)\?"
    
    match = re.search(regex, response.text)
    
    # 检查第二个匹配组 也就是符号
    # 正则表达式中用()划分匹配组
    if match.group(2) == "+":
        answer = int(match.group(1)) + int(match.group(3))
    elif match.group(2) == "-":
        answer = int(match.group(1)) - int(match.group(3))
    elif match.group(2) == "×":
        answer = int(match.group(1)) * int(match.group(3))
    elif match.group(2) == "÷":
        answer = int(match.group(1)) // int(match.group(3))