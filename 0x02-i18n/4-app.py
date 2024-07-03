#!/usr/bin/env python3
"""Module Parametrize templates"""

from flask import Flask, request, render_template
from flask_babel import Babel, _


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__, template_folder = "templates")
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Index route"""
    return render_template('3-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
