from index import app  # Import the Flask app from your index.py

# Expose the Flask app as a WSGI application
if __name__ == "__main__":
    app.run()
