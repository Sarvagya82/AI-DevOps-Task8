from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)
model_path = os.path.join(os.getcwd(), 'iris_model.joblib')
model = joblib.load(model_path)

@app.route('/', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array([data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
