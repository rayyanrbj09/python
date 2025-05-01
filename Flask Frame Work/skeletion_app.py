from flask import Flask 

'''Initialize the Flask application
It creats a Flask application instance
which is the WSGI application callable'''

app = Flask(__name__)

# using a decorator to define a route
# Index page of the application
# / will call the index function
@app.route('/')
def index():
    # Return a simple string response
    return "Hello, World!"

@app.route('/hello/<name>')
def hello(name):
    # Return a personalized greeting
    return f"Hello, {name}!"

# Entry point of the application
if __name__ == '__main__':
    # Run the application
    # The debug=True flag enables the debugger and reloader
    app.run(debug=True)