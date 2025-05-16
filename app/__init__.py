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