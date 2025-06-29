from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained Titanic model
model = joblib.load('best_titanic_model.pkl')

# Health check route
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Titanic model API is running."})

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Parse incoming JSON
    data = request.get_json()

    # Validate input fields
    required_fields = ['Pclass', 'Sex', 'Age', 'Fare']
    if not all(field in data for field in required_fields):
        return jsonify({
            'error': 'Missing one or more required fields: Pclass, Sex, Age, Fare',
            'message': 'Invalid input'
        }), 400

    try:
        # Convert input into array for prediction
        features = [data['Pclass'], data['Sex'], data['Age'], data['Fare']]
        features = np.array([features])  # reshape to (1, 4)

        # Predict using loaded model
        prediction = model.predict(features)[0]

        # Return response
        return jsonify({
            'prediction': int(prediction),  # 0 or 1
            'message': 'Success'
        })

    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'Error during prediction'
        }), 500

# Run app
if __name__ == '__main__':
    app.run(debug=True)
