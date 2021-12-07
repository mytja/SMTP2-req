import requests

# Enable if you use Burpsuite
#import os
#os.environ["HTTP_PROXY"] = "http://127.0.0.1:8082"

uri = "http://127.0.0.1:8080/smtp2/message/delete/32"

headers = {
    "X-Login-Token": open("key.txt", "r").read(),
}

x = requests.delete(uri, headers=headers)
print(x)
print(x.text)
