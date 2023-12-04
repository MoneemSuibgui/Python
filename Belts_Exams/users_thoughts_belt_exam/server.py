from flask_app import app
from flask_app.controllers import users_routes,thoughts_routes,likes_routes


if __name__=="__main__":
    app.run(debug=True)
