from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def home():
    # Return a simple string as the response
    return "Hello, World!"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True) # debug=True allows you to see the changes you make to the code without restarting the server
