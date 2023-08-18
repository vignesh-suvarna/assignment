from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
#Cross-origin resource sharing (CORS) is a browser security feature that restricts cross-origin HTTP requests that are initiated from scripts running in the browser.
CORS(app) 

#Declaring the API route where we'll be hosting it
@app.route('/api/fizzbuzz', methods=['GET'])

#Creating a function named 'fizzbuzz' to write the main logic of the fizzbuzz assignment
def fizzbuzz():
    result = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            result.append('FizzBuzz')
        elif num % 3 == 0:
            result.append('Fizz')
        elif num % 5 == 0:
            result.append('Buzz')
        else:
            result.append(num)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
