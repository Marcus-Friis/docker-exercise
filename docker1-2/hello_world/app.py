from flask import Flask
import os

host = os.environ.get('FLASK_HOST')
port = int(os.environ.get('FLASK_PORT'))

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'din mor'

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
