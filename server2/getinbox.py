import requests
headers = {
    "X-Login-Token": open("key2.txt", "r").read()
}
r = requests.get("http://127.0.0.1:8081/smtp2/message/inbox", headers=headers)
print(r)
print(r.text)
j = r.json()["data"]

message = j[-1]
r = requests.get(message["URI"], headers=headers)
print(r)
print(r.text)
