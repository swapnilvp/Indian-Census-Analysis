# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 07:15:45 2018

@author: USER
"""



# coding: utf-8

# In[2]:
from __future__ import division
from itertools import groupby

import pandas as pd
import operator
import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np




    # In[2]:
def openwindow2():

    # In[3]:


    data = pd.read_csv("india-districts-census-2011.csv")


    # In[4]:


    below_primary=data["Below_Primary_Education"]


    # In[5]:


    total_below_primary=below_primary.sum()


    # In[6]:


    total_below_primary


    # In[7]:


    primary=data["Primary_Education"]


    # In[8]:


    total_primary=primary.sum()


    # In[9]:


    middle=data["Middle_Education"]


    # In[10]:


    total_middle=middle.sum()


    # In[11]:


    secondary=data["Secondary_Education"]
    total_secondary=secondary.sum()


    # In[12]:


    higher=data["Higher_Education"]
    total_higher=higher.sum()
    graduate=data["Graduate_Education"]
    total_graduate=graduate.sum()


    # In[13]:


    population1=data["Population"]


    # In[14]:


    total_population=population1.sum()


    # In[15]:


    per_below_primary=(total_below_primary/total_population)*100


    # In[16]:


    per_primary=(total_primary/total_population)*100


    # In[17]:


    per_secondary=(total_secondary/total_population)*100


    # In[18]:


    per_higher=(total_higher/total_population)*100


    # In[19]:


    per_graduate=(total_graduate/total_population)*100
    per_middle=(total_middle/total_population)*100


    # In[20]:


    edu_groups=[per_below_primary,per_primary,per_middle,per_secondary,per_higher,per_graduate]


    # In[21]:


    label=["BELOW PRIMARY EDUCATION","PRIMARY EDUCATION","MIDDLE EDUCATION","SECONDARY EDUCATION","HIGHER EDUCATION","GRADUATE"]


    # In[22]:


    colors=["green","blue","red","pink","yellow","orange"]


    # In[23]:


    edu_groups


    # In[25]:


    fig, ax = plt.subplots()
    plt.pie(edu_groups,colors=colors,labels=label,autopct='%1.1f%%', shadow=True,startangle=200)
    plt.show()
    fig.savefig('edu.png')




