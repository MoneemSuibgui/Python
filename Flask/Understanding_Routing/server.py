from flask import Flask


app = Flask(__name__)

# Create a root route ("/") that responds with "Hello World!"
@app.route('/')
def index():
    return "Hello World!"


# Create a route that responds with "Dojo!"
@app.route('/dojo')
def dojo():
    return "Dojo!"

# Create a route that responds with "Hi" and whatever name is in the URL after /say/
@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name.capitalize()}!"

# Create a route that responds with the given word repeated as many times as specified in the URL
@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"

    return output

if __name__=="__main__":
    app.run(debug=True)