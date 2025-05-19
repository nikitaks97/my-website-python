from flask import Blueprint, render_template, request

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def index():
    return render_template('index.html')

@app_routes.route('/about')
def about():
    return render_template('about.html')

@app_routes.route('/contact')
def contact():
    return render_template('contact.html')

@app_routes.route('/debug')
def debug():
    import os
    return os.system('ls')  # Security issue: Command injection vulnerability

@app_routes.route('/buggy')
def buggy_route():
    return 1 / 0  # Bug: Division by zero

@app_routes.route('/vulnerable')
def vulnerable_route():
    user_input = request.args.get('input')
    eval(user_input)  # Vulnerability: Use of eval with untrusted input

@app_routes.route('/smelly')
def smelly_route():
    unused_variable = 42  # Code smell: Unused variable
    return 'This route has a code smell'