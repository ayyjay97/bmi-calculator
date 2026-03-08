# BMI Calculator Microservice

## Description

This microservice provides a lightweight backend solution for calculating Body Mass Index (BMI). It listens for HTTP POST requests containing a user's weight in pounds and height in inches. Upon receiving the data, it calculates the BMI and determines the appropriate health category (Underweight, Normal weight, Overweight, or Obese) based on standard thresholds. The service then returns this information in a structured JSON format.

## How to Programmatically REQUEST Data

To request data from this microservice, you must send an HTTP POST request to the `/calculate_bmi` endpoint.

Your request must include a JSON payload with the following key-value pairs:

* `weight_lbs`: A numerical value representing the weight in pounds.

* `height_inches`: A numerical value representing the height in inches.

**Example Request using Python's `requests` library:**

```python
import requests

# Ensure the microservice is running locally on port 5000
url = '[http://127.0.0.1:5000/calculate_bmi](http://127.0.0.1:5000/calculate_bmi)'

# Define the data payload
payload = {
    "weight_lbs": 225,
    "height_inches": 72
}

# Send the POST request
response = requests.post(url, json=payload)
```

## How to Programmatically RECEIVE Data

The microservice processes the request and responds with a JSON object containing the calculated data.

The successful response payload includes two keys:

* `bmi`: A floating-point number representing the calculated BMI, rounded to one decimal place.

* `category`: A string indicating the BMI classification.

**Expected JSON Response:**

```JSON
{
  "bmi": 30.5,
  "category": "Obese"
}
```

**Example of receiving and parsing the data in Python:**

```Python
# Check if the request was successful
if response.status_code == 200:
    # Parse the incoming JSON response
    data = response.json()
    
    # Extract the individual data points
    bmi_value = data['bmi']
    bmi_category = data['category']
    
    print(f"Calculated BMI: {bmi_value}")
    print(f"Health Category: {bmi_category}")
else:
    # Handle any errors returned by the microservice
    error_data = response.json()
    print(f"Error: {error_data.get('error')}")
```
