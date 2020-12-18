"""Script to run some part of my project."""
! pip install --user pillow
! pip install --user playsound
#Package that will import playsound which will allow us to run code thatt plays mp3 files stored in our project.
! pip install --user PyObjC
#Package that is needed to be installed to use playsound.

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')
import string
import random
import nltk


# Imports
from my_module.functions import my_func, my_other_func


###
###

# PYTHON SCRIPT HERE

pass
