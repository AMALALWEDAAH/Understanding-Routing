# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def sayhello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/dojo')
def sayDojo():
    return 'Dojo!'  # Return the string 'Hello World!' as a response


@app.route('/say/<name>')
def sayHello(name):
    return f'Hello {name}'  # Return the string 'Hello World!' as a response


@app.route('/say/<name>/<num>')
def times(name, num):
    return render_template("index.html", _name=name, _num=int(num))


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
