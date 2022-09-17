#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Welcome to Pandas 5')


# In[2]:


import numpy as np
import pandas as pd


# In[3]:


movies = pd.read_csv('movies.csv', index_col=0)
directors=pd.read_csv('directors.csv', index_col=0)


# In[4]:


data = movies.merge(directors, how='left', left_on='director_id', right_on='id')
data.drop(['director_id', 'id_y'], axis=1, inplace=True)


# In[5]:


data


# In[6]:


data['budget'] = (data['budget']/1000000).round(2)
data['revenue'] = (data['revenue']/1000000).round(2)
data


# In[ ]:





# Function is applied to a single column. Hence, the input(can be assumed) is a pandas series.

# In[7]:


def calc_exp(ser):
    ser = ser - ser.mean()
    return ser


# In[8]:


## another way of writing the same above function
def calc_exp(ser):
    ser = ser - np.mean(ser)
    return ser


# In[9]:


data.groupby('director_name')['budget'].transform(calc_exp)


# In[10]:


def exp_bool(df):
    df=np.where(df-df.mean()>0, True, False)
    return df


# In[11]:


data.groupby('director_name')['budget'].transform(exp_bool)


# In[12]:


np.mean(data['budget'])


# In[ ]:





# In[ ]:





# In[13]:


def calc_risky(df):
    df['risky'] = (df['budget'] - df['revenue'].mean()) >=0
    return df


# In[14]:


data_risky = data.groupby('director_name').apply(calc_risky)
data_risky


# In[15]:


data_risky.loc[data_risky['risky'] == True]


# In[16]:


data_risky.loc[data_risky['director_name']=='Marc Forster', ['budget','revenue']]


# In[17]:


data_risky.loc[data_risky['director_name']=='Marc Forster', ['budget','revenue']].mean()


# In[ ]:





# In[ ]:





# In[18]:


data


# In[19]:


data.loc[:, ['revenue', 'budget']]


# In[20]:


data.loc[:, ['revenue', 'budget']].apply(np.sum, axis=0)


# In[21]:


data.loc[:, ['revenue', 'budget']].apply(np.sum, axis=1)


# In[22]:


data.loc[:, ['revenue', 'budget', 'vote_average']].apply('max', axis=0)


# In[ ]:





# In[ ]:





# In[40]:


pfizer = pd.read_csv('Pfizer_1.csv')
pfizer


# In[24]:


pd.Series([1,np.nan,2,np.nan,3])


# In[25]:


pd.Series([1,np.nan,2.0,None,3])


# In[26]:


df=pd.DataFrame({'12':[1,2,np.nan,3,np.nan], '13':[np.nan,23,np.nan,1,2]})


# In[27]:


df


# In[28]:


df[df.isnull().any(axis=1)]


# In[30]:


# df[df.isnull(axis=1)]


# In[31]:


def is_null(x): return sum(x.isnull())


# In[32]:


df.apply(is_null, axis=1)


# In[ ]:





# In[ ]:





# In[33]:


df.isnull()


# In[34]:


df.isna()


# In[36]:


pd.isna


# In[37]:


pd.isnull


# In[41]:


get_ipython().set_next_input('pfizer.isna().sum');get_ipython().run_line_magic('pinfo', 'sum')


# In[43]:


pfizer.isna().sum()


# In[44]:


pfizer.info()


# In[46]:


pfizer.isna().count()


# In[47]:


pfizer.dropna()


# In[49]:


pfizer.dropna(how='all')


# In[51]:


pfizer.fillna(0)


# In[54]:


get_ipython().run_line_magic('pinfo', 'pfizer.fillna')


# In[ ]:





# In[56]:


pd.melt(pfizer, 
       id_vars=['Date', 'Drug_Name', 'Parameter'])


# In[57]:


pd.melt(pfizer, 
       id_vars=['Date', 'Drug_Name', 'Parameter'],
       var_name='Time',
       value_name='Result')


# In[58]:


df_melt = pd.melt(pfizer, 
       id_vars=['Date', 'Drug_Name', 'Parameter'],
       var_name='Time',
       value_name='Result')


# In[59]:


df_melt.pivot(index=['Date', 'Drug_Name', 'Parameter'],
              columns='Time',
              values='Result')


# In[63]:


df_melt.pivot(index=['Date', 'Drug_Name'],
              columns=['Time', 'Parameter'],
              values='Result')


# In[ ]:




