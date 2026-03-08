from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    # Parse the incoming JSON request from the main program
    data = request.get_json()
    
    # Validate the payload
    if not data or 'weight_lbs' not in data or 'height_inches' not in data:
        return jsonify({"error": "Please provide weight_lbs and height_inches in the JSON body."}), 400
        
    try:
        weight = float(data['weight_lbs'])
        height = float(data['height_inches'])
        
        if height <= 0:
            return jsonify({"error": "Height must be greater than zero."}), 400
            
        # Calculate BMI
        bmi = (weight / (height * height)) * 703
        
        # Determine BMI Category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
            
        # Return the JSON response
        return jsonify({
            "bmi": round(bmi, 1),
            "category": category
        }), 200
        
    except ValueError:
        return jsonify({"error": "Invalid input types. Please provide numerical values."}), 400

if __name__ == '__main__':
    # Make sure this port is different from main app port and other services
    port = int(os.environ.get('PORT', 5002))
    app.run(host='0.0.0.0', port=port, debug=True)