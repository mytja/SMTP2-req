import requests

files = [("FILES", open("eicar_com.zip", "rb"))]
r = requests.post("http://172.19.0.3:3000/api/v1/scan", files=files)

print(r)
print(r.text)
