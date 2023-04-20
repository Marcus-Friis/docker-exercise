from flask import Flask
from flask import render_template, request
import requests
import os

host = os.environ.get('FLASK_HOST', '0.0.0.0')
port = int(os.environ.get('FLASK_PORT', 5000))

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == 'POST':
        sentence = request.form.get('sentence')
        response = requests.get(f'http://my_backend:5000?input_str={sentence}').text
        return render_template('home.html', show_results=True, sentiment=response)
    return render_template('home.html', show_results=False)

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
