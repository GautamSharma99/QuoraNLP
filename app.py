from flask import Flask, request, render_template
import pickle

# Load the model and vectorizer
with open('xgb_model.pkl', 'rb') as f:
    xgb_model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        q1 = request.form['question1']
        q2 = request.form['question2']

        # Combine or process questions as per training
        combined = q1 + " " + q2
        vect = vectorizer.transform([combined])
        prediction = xgb_model.predict(vect)[0]

        result = "Duplicate" if prediction == 1 else "Not Duplicate"

    return render_template('index.html', result=result)

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

