#!/usr/bin/env python3


"""Basic Babel Setup"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


# Config class with language and timezone settings
class Config:
    """Configuration for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Apply the configuration to the app
app.config.from_object(Config)

# Instantiate Babel
babel = Babel(app)


@app.route('/')
def index():
    """Handles / Route"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
