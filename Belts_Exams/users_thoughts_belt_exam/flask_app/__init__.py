from flask import Flask
app=Flask(__name__)
app.secret_key="HeyFlask!!!"

db="users_thoughts_schema"