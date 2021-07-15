from typing import Mapping
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hi Pi"

if __name__ == '__main__':
   app.run()