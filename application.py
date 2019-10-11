from flask import Flask, render_template
import json

application = Flask(__name__, template_folder='.')

@application.route('/')
def homepage():
    return render_template('home.html')

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=80, debug=True)
