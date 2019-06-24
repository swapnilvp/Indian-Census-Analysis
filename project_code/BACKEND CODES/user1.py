# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 01:03:18 2018

@author: USER
"""

# coding: utf-8

# In[12]:





# In[13]:


# coding: utf-8

# In[28]:


from __future__ import division
from itertools import groupby
import pandas as pd

import os
import operator
import matplotlib.pyplot as plt
import matplotlib.cm
from pandas import Series,DataFrame


# In[29]:


data=pd.read_csv("file5.csv")


# In[30]:


data.head()


# In[31]:


df=DataFrame(data)


# In[32]:


df


# In[33]:


state=data['State']


# In[34]:


state


# In[35]:


def openwindow(state1):
    stateindex=0

    if (state1=='Uttar Pradesh'):
        stateindex=1
    elif (state1=='Maharastra'):
        stateindex=2
    elif (state1=='Bihar'):
        stateindex=3
    elif (state1=='West Bengal'):
        stateindex=4
    elif (state1=='Andhra Pradesh'):
        stateindex=5
    elif (state1=='Madhya Pradesh'):
        stateindex=6
    elif (state1=='Tamil Nadu'):
        stateindex=7
    elif (state1=='Rajasthan'):
        stateindex=8
    elif (state1=='Karnataka'):
        stateindex=9
    elif (state1==' Gujarat'):
        stateindex=10
    elif (state1=='Orissa'):
        stateindex=11
    elif (state1=='Kerala'):
        stateindex=12
    elif (state1=='Jharkhand'):
        stateindex=13
    elif (state1==' Assam'):
        stateindex=14
    elif (state1=='Punjab'):
        stateindex=15
    elif (state1=='Chhattisgarh'):
        stateindex=16
    elif (state1==' Haryana'):
        stateindex=17
    elif (state1==' Delhi'):
        stateindex=18
    elif (state1==' Jammu and Kashmir'):
        stateindex=19
    elif (state1=='Uttarakhand'):
        stateindex=20
    elif (state1=='Himachal Pradesh'):
        stateindex=21
    elif (state1=='Tripura'):
        stateindex=22
    elif (state1=='Meghalaya'):
        stateindex=23
    elif (state1=='Manipur'):
        stateindex=24
    elif (state1=='Nagaland'):
        stateindex=25
    elif (state1=='Goa'):
        stateindex=26
    elif (state1==' Arunachal Pradesh'):
        stateindex=27
    elif (state1=='Puducherry'):
        stateindex=28
    elif (state1=='Mizoram'):
        stateindex=29
    elif (state1=='Chandigarh'):
        stateindex=30
    elif (state1=='Sikkim'):
        stateindex=31
    elif (state1=='Andaman and Nicobar Islands'):
        stateindex=32
    elif (state1=='Dadra and Nagar Haveli'):
        stateindex=33
    elif (state1==' Daman and Diu'):
        stateindex=34
    elif (state1=='Lakshadweep'):
        stateindex=35
    print(df.ix[stateindex])




