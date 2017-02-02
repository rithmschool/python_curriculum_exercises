from flask import Flask

app = Flask(__name__)

@app.route('/add/<int:num1>/<int:num2>')
def welcome(num1,num2):
    total = num1 + num2
    return str(total)

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1,num2):
    difference = num1 - num2
    return str(difference)

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1,num2):
    product = num1 * num2
    return str(product)

@app.route('/divide/<int:num1>/<int:num2>')
def divide(num1,num2):
    try:
        quotient = num1 / num2
    except ZeroDivisionError:
        return "Please do not divide by 0"
    return str(quotient)

# A BAD SOLUTION - why?
@app.route('/math/<calculation>/<num1>/<num2>')
def math(calculation, num1,num2):

    lookup = {
        "add": '+',
        "subtract": '-',
        "multiply": '*',
        "divide": '/',
    }
    total = num1 + lookup[calculation] + num2
    # Why is this a bad idea?
    return str(eval(total))


# A BETTER OPTION
@app.route('/math/<calculation>/<int:num1>/<int:num2>')
def better_math(calculation, num1,num2):
# A better option
    if calculation == 'add':
        return str(num1+num2)
    elif calculation == 'subtract':
        return str(num1-num2)
    elif calculation == 'multiply':
        return str(num1*num2)
    try:
        quotient = num1 / num2
    except ZeroDivisionError:
        return "Please do not divide by 0"
    return str(quotient)



if __name__ == '__main__':
    app.run(debug=True)





