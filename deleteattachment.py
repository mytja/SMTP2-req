import requests

# Enable if you use Burpsuite
#import os
#os.environ["HTTP_PROXY"] = "http://127.0.0.1:8082"

mid = "0"
aid = "0"

uri = f"http://127.0.0.1:8080/smtp2/attachment/get/{mid}/{aid}"

headers = {
    "X-Login-Token": open("key.txt", "r").read(),
}

x = requests.delete(uri, headers=headers)
print(x)
print(x.text)
