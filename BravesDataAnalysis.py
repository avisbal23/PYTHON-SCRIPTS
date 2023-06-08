#!/usr/bin/env python
# coding: utf-8

# # Braves Data Analysis w/ chatGPT help :)
# 
# ## First - I needed to install necessary packages not delivered in jupyter out of the box

# In[2]:


#pip install seaborn


# ## 2nd - We need to import most necessary libraries 

# In[3]:


# second we need to import most necessary libraries 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# ## 3rd - we need to load the subject data from csv file 
# 

# In[4]:


data = pd.read_csv('https://raw.githubusercontent.com/seanlahman/baseballdatabank/master/core/Teams.csv')


# ## 4th - Now we can explore the data
# 

# In[5]:


# print(data.head(5))
# print("\n\n\n\n\n")
# print("Here is the data column names: ")
# columns = data.columns
# for column in columns:
#     print(column)
# print("\n\n\n\n\n")
# print("Here is the data info now...")
# print(data.info())


# ## 5th - We can now clean the data some 

# In[6]:


# first-we will filter the data to only include the Atlanta Braves
bravesData = data[data['teamID']=='ATL']
# second-we will remove any rows that have missing values 
bravesData.dropna(inplace=True)

# third we can remove any columns that we do not want
bravesData= bravesData.drop(columns=['teamIDretro','teamIDlahman45','teamIDBR','PPF','BPF','franchID','SV','IPouts','FP',"SHO","DP","CS","SF","CG"])


# ## 6th - We can now Analyze the data some

# In[7]:


# First we can use describe method
bravesData.describe()
# for name in bravesData.columns:
#     print(name)


# ## 7th - We then can visualize some of the data 

# #### Histograms for Wins|Losses|RunsScored|RunsAllowed

# In[8]:


###WINS
graphW = sns.histplot(bravesData['W'],bins=15)
plt.title('Distribution of Wins for Atlanta Braves')
plt.xlabel("Wins")


# In[9]:


### Losses
graphL = sns.histplot(bravesData['L'],bins=15)
plt.title('Distribution of Losses for Atlanta Braves')
plt.xlabel("Losses")


# In[10]:


### Losses
graphL = sns.histplot(bravesData['RA'],bins=15)
plt.title('Distribution of Runs Allowed for Atlanta Braves')
plt.xlabel("Runs Allowed")


# #### Line plots for Wins & Losses over the years

# In[11]:


sns.lineplot(data=bravesData,x='yearID',y="W",label="Wins")
plt.title("WINS Over The Years")


# In[12]:


sns.lineplot(data=bravesData,x='yearID',y="L",label="Losses")
plt.title("LOSSES Over The Years")


# #### Scatter plots for Wins & Runs Scored

# In[13]:


sns.scatterplot(data=bravesData,x="R",y="W")
plt.title("Wins vs. Runs Scored for Atlanta Braves")


# In[ ]:





# In[ ]:





# In[ ]:




