import requests

url = "http://challenge-e505c14c195a1140.sandbox.ctfhub.com:10800/flag_in_here/"

for i in range(1,5):
    for j in range(1,5):
        url_final = url + str(i) + "/" + str(j)
        print(url_final)
        result = requests.get(url_final).text
        if "flag.txt" in result:
            print(result)
            print(url_final)
            
            
