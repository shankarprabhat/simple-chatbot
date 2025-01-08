# Flask application for the chatbot
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_flask():
    return 'Hello, flask home!'

@app.route('/home')
def home():
    return 'Hello, World to the LLM Chatbot app!'

@app.route('/about')
def about():
    return 'Trying the about route!'

# Ensure the app runs locally for testing
if __name__ == "__main__":
    app.run(debug=True)