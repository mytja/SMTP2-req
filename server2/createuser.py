import requests
data = {
    "Email": "mytja-test@127.0.0.1:8081",
    "Pass": "test"
}
r = requests.post("http://127.0.0.1:8081/user/new", data=data)
print(r)
print(r.text)
