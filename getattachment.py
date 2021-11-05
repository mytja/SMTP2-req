import requests

mid = "0"
aid = "0"

uri = f"http://127.0.0.1:8080/smtp2/attachment/get/{mid}/{aid}"

headers = {
    "X-Login-Token": open("key.txt", "r").read(),
}

x = requests.get(uri, headers=headers)
if x.status_code == 200:
    with open("responseattachment.png", "wb+") as f:
        f.write(x.content)
else:
    print(x.text)
