"""
This script runs the website_test application using a development server.
"""

from os import environ
from website_test import app

if __name__ == '__main__':
    app.run(debug=True)
