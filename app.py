from flask import Flask
from routes.payments import payments_bp
# from routes.shipping import shipping_bp

def create_app():
    app = Flask(__name__)


    app.register_blueprint(payments_bp, url_prefix="/payments")
    # app.register_blueprint(shipping_bp, url_prefix="/shipping")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=5000, debug=True)