import requests

payload={"name":"NewUser290213"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response.text)