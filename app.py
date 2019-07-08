from flask import Flask, render_template
# from flask.ext.login import LoginManager
from flask_login import login_required
from flask_login import LoginManager


app = Flask(__name__)
login_manager = LoginManager(app)


@app.route('/')
def start():
    return render_template('base.html')


@app.route('/account')
@login_required
def account():
    return 'You are logged in'


if __name__ == '__main__':
    app.run(debug=True)
