#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import libraries needed

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings ('ignore')


# In[3]:


#import dataset

mov = pd.read_csv ('/Users/ivanrodriguez/Desktop/Python Files/A-Z Python for Data Science/P4-Section6-Homework-Dataset.csv', encoding = 'latin1')
#/Users/ivanrodriguez/Desktop/Python Files/A-Z Python for Data Science/P4-Section6-Homework-Dataset.csv


# In[4]:


mov.head()


# In[8]:


mov.describe()


# In[9]:


mov.info()


# In[10]:


# Explore the categorical variable Studio, used in the assignment
mov.Studio.info()


# In[11]:


# Explore the categorical variable Genre, used in the assignment
mov.Genre.info()


# In[24]:


#Interesting pattern: No movie has ever been put out on a Monday. Factorplot is like bars but groups the info.

vis1 = sns.factorplot (data = mov, x= 'Day of Week', kind = 'count', size = 10)


# In[26]:


#Our boxplot only needs 6 studio companies. 
mov.Studio.unique()


# In[28]:


#Our boxplot only needs 5 movie genres. 
mov.Genre.unique()


# In[29]:


# Filter the dataframe by genre. Filter/Subset
mov2 = mov[(mov.Genre == 'action') | (mov.Genre == 'adventure') | (mov.Genre == 'animation') | (mov.Genre == 'comedy') | (mov.Genre == 'drama')]


# In[31]:


mov2 #Data subsetted with the genres we need. 


# In[32]:


# Filter the dataframe by studio. Adding a filter inside a filter (the one above-mov2/mov3). The Studio filter
#on top of our genre filter. 

mov3 = mov2[(mov2.Studio == 'Buena Vista Studios') | (mov2.Studio == 'Fox') | (mov2.Studio == 'Paramount Pictures') | (mov2.Studio == 'Sony') | (mov2.Studio == 'Universal') | (mov2.Studio == 'WB')]


# In[34]:


mov3


# In[35]:


# Check how the filters worked
print (mov2.Genre.unique())
print (mov3.Studio.unique())
print (len(mov2.Genre.unique()))
print (len(mov3.Studio.unique()))


# In[30]:


# w = sns.boxplot (data=movies, x="Genre", y="CriticRating") #Boxplots


# In[37]:


# Define the style: sns.set: customize seaborn theme or use one of six variations of the default theme. 
#Which are called deep, muted, pastel, bright, dark, and colorblind.

sns.set(style="darkgrid", palette="muted", color_codes=True)

# Plot the boxsplots. Variable ax is assigned.

ax = sns.boxplot(data=mov3, x='Genre', y='Gross % US', orient='v', color='lightgray', showfliers=False)
plt.setp(ax.artists, alpha=0.5) #Define transparency

# Add in points to show each observation
sns.stripplot(x='Genre', y='Gross % US', data=mov3, jitter=True, size=6, linewidth=0, hue = 'Studio', alpha=0.7)


ax.axes.set_title('Domestic Gross % by Genre',fontsize=30)
ax.set_xlabel('Genre',fontsize=20)
ax.set_ylabel('Gross % US',fontsize=20)

# Define where to place the legend
ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


# In[ ]:




