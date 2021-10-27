import requests

uri = "http://127.0.0.1:8080/smtp2/message/receive"
data = {
    "Title": "Pozdravi",
    "URI": "http://127.0.0.1:8081/smtp2/message/1",
    "To": "test2@127.0.0.1:8081",
    "From": "test@127.0.0.1:8080",
    "ServerID": "4",
    "ServerPass": "testpass",
}

x = requests.post(uri, headers=data)
print(x)
print(x.text)
