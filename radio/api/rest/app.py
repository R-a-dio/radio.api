from flask import Flask
from flask_peewee.rest import RestAPI


app = Flask(__name__)
app.config.from_object(__name__)

api = RestAPI(app)

from . import register

api.setup()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8050)
