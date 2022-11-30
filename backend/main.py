from flask import Flask
from flask_cors import CORS

from API import api
from Frontend import page as frontend

app = Flask(__name__, template_folder="templates", static_folder="static")
app.register_blueprint(api)
app.register_blueprint(frontend)

CORS(app)  # Enable CORS for the site to allow a frontend on a different IP/port



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
