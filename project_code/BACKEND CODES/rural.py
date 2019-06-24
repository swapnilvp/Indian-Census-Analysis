# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 20:49:02 2018

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
from numpy import *

    # In[2]:
def openwindow7():

    data = pd.read_csv("india-districts-census-2011.csv")


    # In[3]:


    states_group = data.groupby(by = "State name")


    rural_house = []
    urban_house= []

    for key , group in states_group:
        total_rural_house= 0
        total_urban_house = 0

        for row in group.iterrows():

            total_rural_house += row[1][37]
            total_urban_house += row[1][38]

        # Append both values to respective lists
        rural_house.append((key,total_rural_house))
        urban_house.append((key,total_urban_house))

    # Create a dataframe holding state name, male population and female population
    df_household =  pd.DataFrame({
            'state' : [x[0] for x in rural_house] ,
            'rural_house': [x[1] for x in rural_house],
            'urban_house' : [x[1] for x in urban_house]

        })


    df_household


    # In[5]:



    ind = arange(35)
    width = 0.4

    fig, ax = plt.subplots()
    plt.xlim(0,55000000)
    rects1 = ax.barh(ind, df_household['urban_house'],width,color='g',align='center')
    rects2 = ax.barh(ind+width, df_household['rural_house'],width,color='b',align='center')
    ax.set_xlabel('HOUSES')
    ax.set_title('RURAL AND URBAN HOUSES ACROSS DIFFERENT STATES IN INDIA')
    ax.set_yticks(ind + width / 2)
    ax.set_yticklabels((x for x in df_household['state']))
    ax.legend((rects1[0], rects2[0]), ('rural houses', 'urban houses'))
    plt.rcParams.update({'font.size': 20})
    plt.rcParams['figure.figsize'] = (20,20)
    plt.show()
    fig.savefig('rural.png')