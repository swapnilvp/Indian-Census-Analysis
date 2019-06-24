# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 07:32:17 2018

@author: USER
"""


# coding: utf-8

# In[1]:


#Code starts from here
from __future__ import division
from itertools import groupby
import pandas as pd


import operator
import matplotlib.pyplot as plt
import matplotlib.cm
get_ipython().run_line_magic('matplotlib', 'inline')
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
import numpy as np
import seaborn as sns
import math


    # In[2]:
def openwindow3():

    data = pd.read_csv("india-districts-census-2011.csv")


    # In[3]:


    data.groupby('State name').size()


    # In[5]:


    '''
    Calculating state wise literacy rates
    '''

    states_group = data.groupby(by = "State name")

    lpg_rate = []

    for key , group in states_group:

        total_state_pop = 0
        total_lpg_pop = 0

            # Iterating through all the rows for calculating the sum of total population and the literate population

        for row in group.iterrows():
            total_state_pop += row[1][3]
            total_lpg_pop += row[1][33]

        # Calculate literacy rate for the state
        rate1 = (total_lpg_pop/total_state_pop)*100

        # Store the result as a tuple in the list literacy_rate, contaning pairs of state names and literacy rates
        lpg_rate.append((key,rate1))

    print ("Statewise LPG connections are : \n")
    lpg_rate1=pd.Series(lpg_rate)
    lpg_rate1


    # In[17]:


    fig, ax = plt.subplots()

    m = Basemap(projection='merc',lat_0=54.5, lon_0=-4.36,llcrnrlon=68.1, llcrnrlat= 6.5, urcrnrlon=97.4, urcrnrlat=35.5)


    m.drawmapboundary(fill_color='#46bcec')

    m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')

    # Draw coast lines
    m.drawcoastlines()

    # Load the shape file of India
    m.readshapefile("C:\\Users\\USER\\Downloads\\INDIA","INDIA")


    '''
    STEP 4 : CREATING A DATAFRAME MAPPING SHAPES TO STATE NAME AND LITERACY RATES
    '''

    png_rate = []
    #Iterate through INDIA_info file

    for state_info in m.INDIA_info:

        state = state_info['ST_NAME'].upper()    #Converting the state names in upper case
        # initialize rate = 0
        rate = 0

        for x in lpg_rate1:
            if x[0] == state:
                rate = x[1]
                break
        png_rate.append(rate)


    df_poly = pd.DataFrame({
            'shapes': [Polygon(np.array(shape), True) for shape in m.INDIA],
            'area': [area['ST_NAME'] for area in m.INDIA_info],
            'png_rate' : png_rate
        })



    # Get all the shapes
    shapes = [Polygon(np.array(shape), True) for shape in m.INDIA]

    # Create a colormap
    cmap = plt.get_cmap('Reds')

    pc = PatchCollection(shapes, zorder=2)

    norm = Normalize()
    # Set color according to the literacy rate of the state
    pc.set_facecolor(cmap(norm(df_poly['png_rate'].fillna(0).values)))
    ax.add_collection(pc)


    mapper = matplotlib.cm.ScalarMappable(cmap=cmap)
    mapper.set_array(png_rate)
    plt.colorbar(mapper, shrink=0.4)


    ax.set_title("LPG CONNECTIONS IN INDIAN STATES")

    plt.rcParams['figure.figsize'] = (15,15)
    plt.rcParams.update({'font.size': 20})
    plt.show()
    fig.savefig('cng.png')
