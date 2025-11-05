import requests

data = {
    'Close': 11.0,
    'Volume': 1000000,
    'SMA_100': 12.0,
    'RSI_14': 20.0,
    'WTI_Close': 55.32
}

print("Enviando...")
response = requests.post("http://localhost:5001/predict", json=data)
print(response.json())