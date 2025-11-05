import requests

data = {
    'Close': 10.0,
    'Volume': 500000,
    'SMA_100': 12.0,
    'RSI_14': 56.0,
    'Overbought': 0,
    'Oversold': 0,
    'Below_SMA': 1,
    'High_Volume': 1,
    'WTI_Close': 46.32,
    'WTI_Change': 0.02,
    'EC_WTI_Ratio': 0.214,
    'WTI_Volatility': 2.1
}

print("Enviando predicción a http://localhost:5001/predict...")
response = requests.post("http://localhost:5001/predict", json=data)

print(f"Status: {response.status_code}")
if response.status_code == 200:
    print("¡ÉXITO! API FUNCIONANDO:")
    print(response.json())
else:
    print("Error:", response.text)