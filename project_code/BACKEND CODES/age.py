# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 20:57:32 2018

@author: USER
"""

# coding: utf-8

# In[1]:
from __future__ import division
from itertools import groupby


import pandas as pd
import operator
import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np


    # In[2]:
def openwindow8():

    data = pd.read_csv("india-districts-census-2011.csv")


    # In[3]:


    data.shape


    # In[4]:


    young=data["Age_Group_0_29"]


    # In[5]:


    young


    # In[6]:


    total_young=young.sum()


    # In[7]:


    total_young


    # In[8]:


    middle=data["Age_Group_30_49"]
    middle


    # In[9]:


    total_middle=middle.sum()
    total_middle


    # In[10]:


    old=data["Age_Group_50"]


    # In[11]:


    old=data["Age_Group_50"]


    # In[12]:


    old


    # In[13]:


    total_old=old.sum()


    # In[14]:


    total_old


    # In[15]:


    populations1=data["Population"]


    # In[16]:


    total_population=populations1.sum()


    # In[17]:


    total_population


    # In[18]:


    young_per=(total_young/total_population)*100


    # In[19]:


    young_per


    # In[20]:


    old_per=(total_old/total_population)*100


    # In[21]:


    old_per


    # In[22]:


    middle_per=(total_middle/total_population)*100


    # In[23]:


    middle_per


    # In[24]:


    age_groups=[young_per,middle_per,old_per]


    # In[25]:


    age_groups


    # In[26]:


    colors=["green","blue","red"]


    # In[27]:


    label=["Age Group 0 to 29","Age group 30 to 49","Age Group above 50"]
    explode=[0,0.1,0.1]


    # In[31]:

    fig, ax = plt.subplots()
    plt.pie(age_groups,colors=colors,explode=explode,autopct='%1.1f%%', shadow=True, startangle=200,labels=label)
    plt.show()
    fig.savefig('age.png')

