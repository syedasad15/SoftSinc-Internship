from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from
import joblib
import numpy as np

app = Flask(__name__)
swagger = Swagger(app)

# Load trained model
model = joblib.load('best_titanic_model.pkl')

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Titanic model API is running."})

@app.route('/predict', methods=['POST'])
@swag_from({
    'tags': ['Prediction'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'Pclass': {'type': 'integer', 'example': 3},
                    'Sex': {'type': 'integer', 'example': 1, 'description': '1 = male, 0 = female'},
                    'Age': {'type': 'number', 'example': 25},
                    'Fare': {'type': 'number', 'example': 7.25}
                },
                'required': ['Pclass', 'Sex', 'Age', 'Fare']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Prediction successful',
            'examples': {
                'application/json': {
                    'prediction': 0,
                    'message': 'Success'
                }
            }
        },
        400: {
            'description': 'Missing or invalid input'
        },
        500: {
            'description': 'Server error during prediction'
        }
    }
})
def predict():
    data = request.get_json()

    required_fields = ['Pclass', 'Sex', 'Age', 'Fare']
    if not all(field in data for field in required_fields):
        return jsonify({
            'error': 'Missing required fields: Pclass, Sex, Age, Fare',
            'message': 'Invalid input'
        }), 400

    try:
        features = np.array([[data['Pclass'], data['Sex'], data['Age'], data['Fare']]])
        prediction = model.predict(features)[0]

        return jsonify({
            'prediction': int(prediction),
            'message': 'Success'
        })

    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'Error during prediction'
        }), 500 

if __name__ == '__main__':
    app.run(debug=True)
