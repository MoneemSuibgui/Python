from flask import Flask, render_template


app = Flask(__name__)

# create the /play route render a template with 3 blue boxes
@app.route('/play')
def level_one():
    return render_template("index.html",num=3,color="blue")

# Have the /play/<x> route render a template with x number of blue boxes
@app.route('/play/<int:num>')
def level_two(num):
    return render_template("index.html", num=num, color="blue")

# Have the /play/<x>/<color> route render a template with x number of boxes the color of the provided value
@app.route('/play/<int:num>/<string:color>')
def level_three(num, color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)