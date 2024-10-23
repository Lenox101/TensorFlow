from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
model = pickle.load(open('insurance_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('insurance_model.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    age = (int(request.form.get('age'))) / 100
    affordability = int(request.form.get('affordability'))

    input_data = pd.DataFrame({
                'age': [age],
                'affordability': [affordability]
    })


   # Make prediction and flatten the result
    prediction = model.predict(input_data)[0][0]  # Access the first element of the first sub-array

     # Convert prediction to a percentage and format it
    prediction_percentage = prediction * 100
    formatted_prediction = f'{prediction_percentage:.2f}%'  # Format to two decimal places

    return render_template('insurance_model.html', prediction_text=f'Application Prediction: {formatted_prediction}')

if __name__ == '__main__':
    app.run(debug=True)