# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 07:41:58 2018

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
import numpy as np;
from numpy import *


    # In[2]:

def openwindow4():
    # Load dataset
    data = pd.read_csv("india-districts-census-2011.csv")


    # In[3]:



    states_group = data.groupby(by = "State name")


    male_popu = []
    female_popu= []

    for key , group in states_group:
        total_male_popu= 0
        total_female_popu = 0

        for row in group.iterrows():

            total_male_popu += row[1][4]
            total_female_popu += row[1][5]

        # Append both values to respective lists
        male_popu.append((key,total_male_popu))
        female_popu.append((key,total_female_popu))

    # Create a dataframe holding state name, male population and female population
    df_sex_ratio =  pd.DataFrame({
            'state' : [x[0] for x in male_popu] ,
            'male_popu': [x[1] for x in male_popu],
            'female_popu' : [x[1] for x in female_popu]

        })


    df_sex_ratio


    # In[5]:



    ind = arange(35)
    width = 0.4

    fig, ax = plt.subplots()
    plt.xlim(0,100000000)
    rects1 = ax.barh(ind, df_sex_ratio['female_popu'],width,color='g',align='center')
    rects2 = ax.barh(ind+width, df_sex_ratio['male_popu'],width,color='b',align='center')
    ax.set_xlabel('Population')
    ax.set_title('MALE AND FEMALE POPULATION ACROSS DIFFERENT STATES IN INDIA')
    ax.set_yticks(ind + width / 2)
    ax.set_yticklabels((x for x in df_sex_ratio['state']))
    ax.legend((rects1[0], rects2[0]), ('Male population', 'Female population'))
    plt.rcParams.update({'font.size': 20})
    plt.rcParams['figure.figsize'] = (20,20)
    plt.show()
    fig.savefig('sexratio.png')
