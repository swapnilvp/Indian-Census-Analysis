# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 11:23:29 2018

@author: USER
"""


# coding: utf-8

# In[39]:
from __future__ import division
from itertools import groupby

import pandas as pd
import operator
import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np
from pandas import Series,DataFrame
from numpy import *


# In[71]:


data = pd.read_csv("book2.csv")


# In[72]:


df=DataFrame(data)


# In[73]:


df


# In[33]:

def openwindow(Parameter1,Parameter2):



    df=DataFrame(data,columns=['state'])
    df['state']


    # In[86]:


    df1=DataFrame(data,columns=[Parameter1,Parameter2])
    df1.astype('int64')
    df1


    # In[92]:



    ind = arange(35)
    width = 0.4

    fig, ax = plt.subplots()
    plt.xlim(0,199,812,341)
    rects1 = ax.barh(ind, df1[Parameter1],width,color='g',align='center')
    rects2 = ax.barh(ind+width, df1[Parameter2],width,color='b',align='center')
    ax.set_xlabel('HOUSES')
    ax.set_yticks(ind + width / 2)
    ax.set_yticklabels((x for x in df['state']))
    ax.legend((rects1[0], rects2[0]), (Parameter1,Parameter2))
    plt.rcParams.update({'font.size': 20})
    plt.rcParams['figure.figsize'] = (20,20)
    plt.show()
    fig.savefig('user.png')
