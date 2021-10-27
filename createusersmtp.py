import requests
data = {
    "Email": "mytja@127.0.0.1:8080",
    "Pass": "test"
}
r = requests.post("http://127.0.0.1:8080/user/new", data=data)
print(r)
print(r.text)
