"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import website_test.views
#import spacy
#from . import module1
#from . import module2
#from . import find3
#from . import numb