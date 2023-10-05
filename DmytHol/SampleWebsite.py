from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route and a function to handle the route
@app.route('/')
def hello_world():
    return 'Hello, World! Test'

# Run the Flask application
if __name__ == '__main__':
    app.run()