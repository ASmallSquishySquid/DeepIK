from distutils.core import setup # Need this to handle modules

import py2exe

import ctypes
from numpy import array, savetxt
from tkinter import *
from tkinter import messagebox
from keras.models import load_model # source of errors
from os import scandir, remove, makedirs
from PIL import Image, ImageDraw

setup(console=['main.py']) # Calls setup function to indicate that we're dealing with a single console application

# errors:
# pkg_resources._vendor.pyparsing.ParseException: Expected stringEnd
# pkg_resources.extern.packaging.requirements.InvalidRequirement: Parse error at "'__'": Expected stringEnd