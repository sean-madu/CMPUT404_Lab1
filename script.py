import requests

url = "https://raw.githubusercontent.com/sean-madu/CMPUT404_Lab1/main/script.py"
data = requests.get(url)
print(data.text)
