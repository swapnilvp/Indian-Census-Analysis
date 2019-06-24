# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 08:04:04 2018

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


    # In[7]:
def openwindow6():

    data = pd.read_csv("india-districts-census-2011.csv")


    # In[8]:


    data.shape


    # In[9]:


    hindus1= data["Hindus"]


    # In[10]:


    hindus1


    # In[11]:


    total_hindus=hindus1.sum()


    # In[12]:


    total_hindus


    # In[13]:


    muslims1=data["Muslims"]


    # In[14]:


    total_muslims=muslims1.sum()


    # In[15]:


    total_muslims


    # In[16]:


    sikhs1=data["Sikhs"]


    # In[17]:


    total_sikhs=sikhs1.sum()


    # In[18]:


    total_sikhs


    # In[19]:


    christians1=data["Christians"]


    # In[20]:


    total_christians=christians1.sum()


    # In[21]:


    total_christians


    # In[22]:


    buddhists1=data["Buddhists"]


    # In[23]:


    total_buddhists=buddhists1.sum()


    # In[24]:


    total_buddhists


    # In[25]:


    jains1=data["Jains"]


    # In[26]:


    total_jains=jains1.sum()


    # In[27]:


    total_jains


    # In[28]:


    populations1=data["Population"]


    # In[29]:


    total_population=populations1.sum()


    # In[30]:


    total_population


    # In[31]:


    hindu_per=(total_hindus/total_population)*100


    # In[32]:


    hindu_per


    # In[33]:


    muslims_per=(total_muslims/total_population)*100


    # In[34]:


    muslims_per


    # In[35]:


    sikhs_per=(total_sikhs/total_population)*100


    # In[36]:


    sikhs_per


    # In[37]:


    christians_per=(total_christians/total_population)*100


    # In[38]:


    christians_per


    # In[39]:


    buddhists_per=(total_buddhists/total_population)*100


    # In[40]:


    buddhists_per


    # In[41]:


    jains_per=(total_jains/total_population)*100


    # In[42]:


    jains_per


    # In[43]:


    religions=[hindu_per,muslims_per,sikhs_per,buddhists_per,christians_per,jains_per]


    # In[44]:


    religions


    # In[45]:


    colors=["orange","green","yellow","blue","purple","red"]


    # In[46]:


    label=["HINDUS","MUSLIMS","SIKHS","BUDDHISTS","CHRISTIANS","JAINS"]


    # In[48]:

    fig, ax = plt.subplots()
    plt.pie(religions,colors=colors,autopct='%1.1f%%', shadow=True, startangle=200,labels=label)
    plt.show()
    fig.savefig('religions.png')
