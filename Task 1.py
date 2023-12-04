#!/usr/bin/env python
# coding: utf-8

# # Task 1 
# - Create a bar chart or histogram to visualize the distribution of a 
# - categorical or continuous variable, such as the distribution of 
# - ages or genders in a population.

# # Importing Libraries

# In[1]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")


# In[2]:


#reading the DataFrame
car=pd.read_csv('cars.csv')
car


# In[3]:


car.info()


# # visualization

# In[4]:


car.head()


# In[5]:


# checking the relationship between width and price of cars
plt.figure(figsize=(10,10))
x=car['width'] # independent variable
y=car['price'] # dependent vari
plt.scatter(x,y)
plt.xlabel("Width of car")
plt.ylabel("Price of car")
plt.title("Width v/s Price of car")
plt.show()


# In[6]:


# ploting histogram in categorical ani numerical data
# fuel-type coli=umn
plt.hist(car['fuel-type'])
plt.xlabel('Fuel-type')
plt.ylabel('No of cars')
plt.title('price v/s no of cars')
c=car['fuel-type'].value_counts()
plt.yticks(c)
plt.show()


# In[7]:


# Barplot()
car['fuel-type'].value_counts().plot(kind='bar')
plt.show()


# In[ ]:




