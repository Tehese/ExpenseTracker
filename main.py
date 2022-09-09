# Scott Canfield
# September 8th, 2022
# Project Idea
# Take Bank Statements in the form of CSV Files, clean them up into Months, Categories, and Totals
# Then from there Calculate how you spent each month in each category
# Be able to drop them into a webpage, SAFELY(Encrypton more than likely) , and then have it calculate everything you need and display it to a webpage
# We want Pie Graphs!!!!!!

import numpy as np
import panda as pd
from cryptography.fernet import Fernet
from datetime import date

# The moment the user inputs the file we need to encrypt it,
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
