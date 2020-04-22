from flask import Flask
from pony.flask import Pony
from pony.orm import Database

app = Flask(__name__)
Pony(app)

db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

@app.route('/')
def hello_world():
    return 'Hello, World!'


db.generate_mapping(create_tables=True)
