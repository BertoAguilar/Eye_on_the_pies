from flask_app import app
from flask_app.controllers import users, pies
from flask import url_for

@app.route("/favicon.ico")
def favicon():
    return url_for('static', filename='data:,')
if __name__=="__main__":
    app.run(debug=True)