from flask import Flask, render_template, request, redirect, url_for, jsonify
import math
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])
def math_ops():
    if request.method == 'POST':
        ops = request.form['operation']
        num1 = request.form['num1']
        num2 = request.form['num2']

        if ops == 'add':
            r = int(num1) + int(num2)
            result = "The sum of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if ops == 'subtract':
            r = int(num1) - int(num2)
            result = "The difference of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if ops == 'multiply':
            r = int(num1) * int(num2)
            result = "The product of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if ops == 'divide':
            r = int(num1) / int(num2)
            result = "The quotient when " + str(num1) + " is divided by " + str(num2) + " is " + str(r)
        if ops == 'log':
            r = math.log(int(num1), int(num2))
            result = "The logarithm of " + str(num1) + " to the base " + str(num2) + " is " + str(r)

        # return jsonify(result)
        return render_template('results.html', result=result)
            

@app.route('/postman_action', methods=['POST'])
def postman_action():
    if request.method == 'POST':
        ops = request.json['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']

        if ops == 'add':
            r = int(num1) + int(num2)
            result = "The sum of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if ops == 'subtract':
            r = int(num1) - int(num2)
            result = "The difference of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if ops == 'multiply':
            r = int(num1) * int(num2)
            result = "The product of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if ops == 'divide':
            r = int(num1) / int(num2)
            result = "The quotient when " + str(num1) + " is divided by " + str(num2) + " is " + str(r)
        if ops == 'log':
            r = math.log(int(num1), int(num2))
            result = "The logarithm of " + str(num1) + " to the base " + str(num2) + " is " + str(r)
        return jsonify(result)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
