# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 20:31:52 2015

@author: aditya
"""

#Import all packages required for this exercise

import nltk
# Check NLTK Version. Must be 2.0.5 to go with Python 2.7
print('The nltk version is {}.'.format(nltk.__version__))
# Download everything from nltk
#nltk.download()
#If you did not install the data to one of the above central locations
#Then nltk.data.path.append("path to nltk_data")


import os
import json
import unicodedata
import string
import io
import pandas as pd
import textmining
import sklearn
import numpy as np
global collections
import collections
global operator
import operator
global create_tag_image
global make_tags
global LAYOUTS
global get_tag_counts

from nltk import *
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import stem

from sklearn.feature_extraction.text import CountVectorizer
from pytagcloud import create_tag_image, make_tags, LAYOUTS
from pytagcloud.lang.counter import get_tag_counts

print 'finish' 


# Now let's try to process one article first
# For Mac users#
# If pygame is not found, please run the follows at IPython console:

# ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# brew install sdl sdl_ttf sdl_image sdl_mixer portmidi
# conda install binstar
# conda install -c https://conda.binstar.org/quasiben pygame




