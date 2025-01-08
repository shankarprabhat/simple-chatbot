# Flask application for the chatbot
from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return 'Hello, World to the LLM Chatbot app!'

@app.route('/about')
def about():
    return 'Trying the about route!'
