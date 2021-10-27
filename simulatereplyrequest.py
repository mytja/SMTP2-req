import requests

# Enable if you use Burpsuite
#import os
#os.environ["HTTP_PROXY"] = "http://127.0.0.1:8082"

uri = "http://127.0.0.1:8081/smtp2/message/receive"
headers = {
    "Title": "RE: Pozdravi",
    "Body": "Se eni pozdravi - tokrat iz bodyja - in to drugic.",
    "To": "mytja-test@127.0.0.1:8081",
    "From": "mytja@127.0.0.1:8080",
    "ReplyPass": "u4WzwBE2dDEi0aAPgPEho2z8dUarNDgom845GacQgE1r6vt8B5",
    "ReplyID": "Djw7ImGhJAPH9XevlQPzVG8LJULf5JXRQKivAHdMChNjpciFMQ",
    "OriginalID": "10",
    "ServerID": "199",
    "ServerPass": "passsssssss",
    "URI": "http://127.0.0.1:8080/smtp2/message/get/199?pass=passsssssss"
}

x = requests.post(uri, headers=headers)
print(x)
print(x.text)
