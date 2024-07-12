#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    html = ''
    for i in range(parameter):
        html += f'{i}\n'
    return f'{html}'

@app.route('/math/<num1>/<operation>/<num2>')
def match(num1, operation, num2):
    num1 = int(num1)
    num2 = int(num2)
    if operation == '+':
        return f'{num1 + num2}'
    elif operation == '-':
        return f'{num1 - num2}'
    elif operation == '*':
        return f'{num1 * num2}'
    elif operation == 'div':
        return f'{num1 / num2}'
    elif operation == '%':
        return f'{num1 % num2}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
