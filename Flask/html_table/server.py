from flask import Flask, render_template

app = Flask(__name__)

# Create a route in which the data above is declared and then sent to the template engine to be rendered
@app.route('/')
def index():
    users = [
        {'first_name' : 'Choi', 'last_name' : 'Choi'},
        {'first_name' : 'Moneem', 'last_name' : 'Suibgui'},
        {'first_name' : 'Kamle', 'last_name' : 'Suibgui'},
        {'first_name' : 'Lionel', 'last_name' : 'Messi'}
    ]
    return render_template("index.html",users=users)



if __name__=="__main__":
    app.run(debug=True,port=5022)