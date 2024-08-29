#!/usr/bin/env python3


"""Get Locale from request"""

from flask import Flask, render_template, request
from flask_babelex import Babel

app = Flask(__name__)


# Config class with language and timezone settings
class Config:
    """Language Configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Apply the configuration to the app
app.config.from_object(Config)


# Instantiate Babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Handles / Route"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)
