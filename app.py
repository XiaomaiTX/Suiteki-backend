#!/usr/bin/python
from flask import Flask
import sqlite3
suiteki = Flask(__name__)
db_con = sqlite3.connect('suiteki_backend.db')
@suiteki.route('/api')
def hello_world():
    return 'Hello World'
if __name__ == '__main__':
    suiteki.run()