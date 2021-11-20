import requests

# Enable if you use Burpsuite
#import os
#os.environ["HTTP_PROXY"] = "http://127.0.0.1:8082"

uri = "http://127.0.0.1:8080/smtp2/message/new"
data = {
    "DraftID": "4"
}

headers = {
    "X-Login-Token": open("key.txt", "r").read()
}

x = requests.post(uri, data=data, headers=headers)
print(x)
print(x.text)
