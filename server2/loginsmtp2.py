import requests
data = {
    "Email": "mytja-test@127.0.0.1:8081",
    "Pass": "test"
}
r = requests.post("http://127.0.0.1:8081/user/login", data=data)
print(r)
with open("key2.txt", "w+") as f:
    f.write(r.text)
