# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 21:49:22 2018
@author: Gupta2 Abhishek
"""

#importing the libraries
import os
import sys

print(sys.version)
print("My first python code")

#calculating sum of two numbers
x=2
y=4

print("Sum of two numbers is {}".format(x+y))


#creating pandas DataFrame
import pandas as pd

data=pd.DataFrame.from_dict(data={'A':{0:1,1:2,2:3},
                             'B':{0:3,1:4,2:5},
                             'C':{0:7,1:8,2:9}
                             })

data.head(1)