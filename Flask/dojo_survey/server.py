from flask import Flask, render_template, session, redirect,request

app = Flask(__name__)

app.secret_key="Iam here Flask!!!!"

# Have the root route ("/") show a page with the form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process',methods=['POST'])
def process():
    # Put the form data into session
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/success')

# Have the "/success" route display the information from the form on a new HTML page
@app.route('/success')
def success():
    return render_template('success.html')
    
if __name__=="__main__":
    app.run(debug=True,port=5022)