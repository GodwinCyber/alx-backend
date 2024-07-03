#!/usr/bin/env python3
"""Module Parametrize templates"""

from typing import Union
from flask import Flask, request, render_template, g, abort
from flask_babel import Babel, _

# mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages"""
    locale = request.args.get('locale', '')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])

def get_user() -> Union[dict, None]:
    """Define a get_user function that returns a user dictionary or
       None if the ID cannot be found or if login_as was not passed.
    """
    login_user = request.args.get('login_as')
    if login_user:
        try:
            user_id = int(login_user)
            return users.get(user_id)
        except ValueError:
            return None
    else:
        return None

@app.before_request
def before_request():
    """Define a before_request function and use the 
       app.before_request decorator to make it be
       executed before all other functions. before_request
       should use get_user to find a user if any, and
       set it as a global on flask.g.user
    """
    g.user = get_user()

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Index route"""
    return render_template('5-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
