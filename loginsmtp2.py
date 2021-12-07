import requests

# Enable if you use Burpsuite
#import os
#os.environ["HTTP_PROXY"] = "http://127.0.0.1:8082"

data = {
    "Email": "mytja@127.0.0.1:8080",
    "Pass": "test"
}
r = requests.post("http://127.0.0.1:8080/smtp2/user/login", data=data)
print(r)
with open("key.txt", "w+") as f:
    f.write(r.json()["data"])
