from flask import Flask
from flask_cors import CORS
from main.routes import api

app = Flask(__name__)

CORS(
    app,
    resources={
        r"/v1/*": {
            "origins": ["https://localhost", "http://localhost", "capacitor://localhost"],
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    }
)

app.register_blueprint(api, url_prefix='/v1')

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'


if __name__ == '__main__':
    app.run(debug=True)

