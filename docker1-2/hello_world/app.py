from flask import Flask
import os

host = os.environ.get('FLASK_HOST', '0.0.0.0')
port = int(os.environ.get('FLASK_PORT', 5000))

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'din mor'

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
