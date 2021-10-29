import requests

# Enable if you use Burpsuite
#import os
#os.environ["HTTP_PROXY"] = "http://127.0.0.1:8082"

uri = "http://127.0.0.1:8080/smtp2/draft/new"

headers = {
    "X-Login-Token": open("key.txt", "r").read(),
    "ReplyTo": ""
}

x = requests.post(uri, headers=headers)
print(x)
print(x.text)
