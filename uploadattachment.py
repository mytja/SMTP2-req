import requests

# Enable if you use Burpsuite
#import os
#os.environ["HTTP_PROXY"] = "http://127.0.0.1:8082"

uri = "http://127.0.0.1:8080/smtp2/attachment/upload/0"

headers = {
    "X-Login-Token": open("key.txt", "r").read(),
}

files = {'file': open('meetplanlogo.png', 'rb')}

x = requests.post(uri, headers=headers, files=files)
print(x)
print(x.text)
