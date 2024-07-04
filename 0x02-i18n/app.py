#!/usr/bin/env python3
"""Module  Display the current time"""

from typing import Union, Dict
from flask import Flask, request, render_template, g
from flask_babel import Babel, format_datetime
import pytz
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime


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

    user = getattr(g, 'user', None)
    if user and user['locale'] in app.config['LANGUAGES']:
        return user['locale']

    locale = request.headers.get('locale', '')
    if locale and locale in app.config["LANGUAGES"]:
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


@babel.timezoneselector
def get_timezone():
    """Get timezone function and use the babel.timezoneselector
       decorator. The logic should be the same as get_locale:
       Find timezone parameter in URL parameters
       Find time zone from user settings
       Default to UTC
       Before returning a URL-provided or user time zone, you must
       validate that it is a valid time zone. To that, use
       pytz.timezone and catch the
       pytz.exceptions.UnknownTimeZoneError exception.
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass

    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Index route"""
    current_time = datetime.now(pytz.timezone(get_timezone()))
    formatted_time = format_datetime(current_time)
    return render_template('index.html', current_time=formatted_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
