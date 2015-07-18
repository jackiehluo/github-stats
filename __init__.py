from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine(app)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')