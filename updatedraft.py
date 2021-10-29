import requests

# Enable if you use Burpsuite
#import os
#os.environ["HTTP_PROXY"] = "http://127.0.0.1:8082"

uri = "http://127.0.0.1:8080/smtp2/draft/save"

headers = {
    "X-Login-Token": open("key.txt", "r").read(),
}

data = {
    "ID": "0",
    "To": "mytja-test@127.0.0.1:8081",
    "Body": "Hehej",
    "Title": "Zelo resen pozdrav"
}

x = requests.post(uri, data=data, headers=headers)
print(x)
print(x.text)
