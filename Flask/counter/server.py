from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key="hello flask,iam Moneem!!"


# the root route "/" render a template that displays the number of times the client has visited this site. Refresh the page several times to ensure the counter is working
@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

# Add a "/reset" route that clears the session and redirects to the root route
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True,port=5011)