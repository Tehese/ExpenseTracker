# Scott Canfield
# September 8th, 2022
# Project Idea
# Take Bank Statements in the form of CSV Files, clean them up into Months, Categories, and Totals
# Then from there Calculate how you spent each month in each category
# Be able to drop them into a webpage, SAFELY(Encrypton more than likely) , and then have it calculate everything you need and display it to a webpage
# We want Pie Graphs!!!!!!

import numpy as np
import panda as pd
from    matplotlib import pyplot as plt
from cryptography.fernet import Fernet
from datetime import date

# The moment the user inputs the file we need to encrypt it,
