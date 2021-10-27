import requests
headers = {
    "X-Login-Token": open("key.txt", "r").read()
}
r = requests.get("http://127.0.0.1:8080/smtp2/message/inbox", headers=headers)
print(r)
j = r.text
print(j)
