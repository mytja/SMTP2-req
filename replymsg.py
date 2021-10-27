import requests

# Enable if you use Burpsuite
#import os
#os.environ["HTTP_PROXY"] = "http://127.0.0.1:8082"

uri = "http://127.0.0.1:8080/smtp2/message/reply/10"
data = {
    "Title": "RE: Pozdravi",
    "Body": "Še eni pozdravi - tokrat iz bodyja - in to drugič.",
}

headers = {
    "X-Login-Token": open("key.txt", "r").read()
}

x = requests.post(uri, data=data, headers=headers)
print(x)
print(x.text)
