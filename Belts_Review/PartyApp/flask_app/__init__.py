from flask import Flask

app = Flask(__name__)

# ! Add session & Database name

app.secret_key = "Trust the process"

DATABASE = "parties_db"