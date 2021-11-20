import requests

# Enable if you use Burpsuite
#import os
#os.environ["HTTP_PROXY"] = "http://127.0.0.1:8082"

uri = "http://127.0.0.1:8080/smtp2/message/update"

headers = {
    "X-Login-Token": open("key.txt", "r").read(),
}

data = {
    "ID": "4",
    "To": "mytja-test@127.0.0.1:8081;mytja-test@127.0.0.1:8082",
    "Body": "Hehej",
    "Title": "Zelo resen pozdrav"
}

x = requests.patch(uri, data=data, headers=headers)
print(x)
print(x.text)
