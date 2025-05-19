from flask import Flask

def create_app():
    app = Flask(__name__)
    from .routes import app_routes
    app.register_blueprint(app_routes)
    
    return app

app = create_app()

if __name__ == "__main__":
    from routes import app_routes
    app = Flask(__name__)
    app.register_blueprint(app_routes)
    app.run(host="0.0.0.0", port=5002)

def insecure_function():
    password = 'hardcoded_password'  # Security issue: Hardcoded sensitive information
    print(password)

def buggy_function():
    return [1, 2, 3][5]  # Bug: Index out of range

def vulnerable_function():
    import pickle
    data = pickle.loads(b"malicious_data")  # Vulnerability: Unsafe deserialization

def smelly_function():
    for i in range(10):
        pass  # Code smell: Empty loop body