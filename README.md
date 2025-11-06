Stock Price Movement Prediction with Machine Learning

This academic project applies Machine Learning techniques to predict whether a stock's price will go up or down the next day, using historical data and supervised models. The approach is practical, featuring a functional API, Dockerized environment, and a trained model ready to make predictions based on user-provided inputs.

🎯 Project Objective

To develop a binary prediction system (up / down) for stock price movement, based on features extracted from historical data. The model was trained, evaluated, and deployed via an API to facilitate integration.

📁 Project Structure

File / Folder	Description

	stock_pred_ec_oil.ipynb	Main notebook with data exploration, model training, and evaluation.
	app.py	Script exposing the model as a REST API using FastAPI.
	test_api.py	Unit tests to validate API functionality.
	requirements.txt	List of dependencies required to run the project.
	Dockerfile	Configuration for containerizing the application.
	DATA/	Folder containing the data used to train the model.
	best_model.pkl	Trained and serialized model ready to be loaded by the API.
	README.md	Project documentation.

🛠️ Technologies Used

    Python 3.10+
    Scikit-learn
    Pandas / NumPy
    FastAPI
    Docker
    Pytest

📊 Example Usage

Once the API is running, you can send a POST request with the following input features:
json

{
  "Close": 10.0,  
  "Volume": 500000,
  "SMA_100": 12.0,
  "RSI_14": 56.0,
  "WTI_Close": 46.32
}

The response will be:

json
{
  "prediction": 1,
  "confidence": 0.6,
  "meaning": "1 = DOWN tomorrow"
}

🔍 Input Explanation

    Close: Closing price of the stock on the last trading day.
    Volume: Number of shares traded at the close of the last trading day.
    SMA_100: 100-period Simple Moving Average at the close of the last trading day.
    RSI_14: Relative Strength Index (14-period) at the close of the last trading day.
    WTI_Close: Closing price of WTI crude oil on the last trading day.

📈 Results

The model achieved an accuracy of 53.1% on the test set, using a classifier [specify: RandomForest, XGBoost, etc.]. It was evaluated using metrics such as accuracy, F1-score, and confusion matrix.

🧪 How to run the prediction model with Docker

The model runs with  Conda and  Docker and the test needs to use the file  test_api.py. Follow the next stpes:

🧪 Cómo correr el modelo de predicción
Sigue estos pasos para clonar el repositorio, construir el contenedor Docker, y obtener una predicción desde la API.

1️⃣ Clonar el repositorio
bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

2️⃣ Activar el entorno Conda (opcional si solo usas Docker)
Si deseas usar el entorno Conda localmente:
bash
conda activate nombre_del_entorno
Asegúrate de tener el entorno creado previamente. Si no lo tienes, puedes crearlo con:
bash
conda create -n nombre_del_entorno python=3.8
conda activate nombre_del_entorno
pip install -r requirements.txt

3️⃣ Construir el contenedor Docker
bash
docker build -t ec-wti-api .
Este comando puede tardar unos segundos. El punto (.) al final es obligatorio.

4️⃣ Correr el contenedor Docker
```bash
docker run -p 5001:5000 ec-wti-api
```
Esto inicia la API en el puerto 5000 dentro del contenedor, expuesto como 5001 en tu máquina local.

5️⃣ Probar la API desde otra terminal
Abre una segunda terminal (con el mismo entorno activado si usas Conda) y ejecuta:
bash
python test_api.py
Esto enviará una solicitud a la API y mostrará una predicción como:
json
{
  "prediction": 0,
  "confidence": 0.72,
  "meaning": "0 = SUBE mañana"
}
🧠 Notas adicionales
Asegúrate de tener Docker instalado: Instalar Docker
El archivo test_api.py debe estar en la raíz del repositorio o en la carpeta indicada.
Si el puerto 5001 está ocupado, puedes cambiarlo en el comando docker run

📦 Model Files

    Dockerfile
    requirements.txt
    app.py (with 5 inputs + automatic feature calculation)
    test_api.py
    best_model.pkl
    data/features.pkl
    README.md

🧾 Additional Notes

    NaN values handled via dropna()
    Only 5 inputs required — API computes additional features
    Accuracy: 53.1% (+2.5% improvement with WTI feature)
    Model serialized with joblib (preferred over pickle)

🎓 Credits

This project was developed as part of the Machine Learning Zoomcamp course by DataTalksClub (https://github.com/DataTalksClub/machine-learning-zoomcamp/), for educational and practical exploration in data science and machine learning.