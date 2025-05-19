from flask import Blueprint, render_template

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