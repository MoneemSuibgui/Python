from flask_app import app



if __name__ =='__main__':
    app.run(debug=True, port=5001)
    # ! Don't Forget To Import All* controllers (Routes)
from flask_app.controllers import users , parties