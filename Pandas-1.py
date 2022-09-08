#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Welcome to Pandas-1')


# In[2]:


import pandas as pd


# In[3]:


df=pd.read_csv('gapminder.csv')


# In[4]:


df


# In[5]:


df['population'].argmax()


# In[6]:


df.iloc[200]


# In[7]:


type(df)


# In[8]:


df['country'] #method1


# In[9]:


df.country #method2


# In[10]:


# method2 is preferred to method1


# In[11]:


df[['country', 'year']]


# In[12]:


df[['country']]


# In[13]:


df.head()


# In[14]:


df.tail()


# In[15]:


df.head(10)


# In[16]:


df.head(-5)


# In[17]:


df.tail(-10)


# In[18]:


df.shape


# In[19]:


df.head(2)


# In[20]:


df1 = pd.DataFrame([['Afghanistan', 1952, 8425333, 'Asia', 28.801, 779.445314], 
              ['Afghanistan', 1957, 9245333, 'Asia', 30.801, 820.850314]
             ],
              columns=['country', 'year', 'population', 'continent', 'life_exp', 'gdp_cap'])


# In[21]:


df1


# In[22]:


df2=pd.DataFrame({'country': ['Afg', 'Afg'],
              'year': [1952, 1957],
              'population' : [8425333, 9240934],
              'contintent': ['Asia', 'Asia'],
              'life_exp': [28.801, 30.332],
              'gdp_cap': [779.445314, 820.8503030]})


# In[23]:


df2


# In[24]:


type(df.columns)


# In[25]:


df.columns


# In[26]:


df.keys()


# In[27]:


df.values


# In[ ]:





# In[28]:


df['country'].head()


# In[29]:


df[['gdp_cap', 'year']].head()


# In[30]:


df['country'].unique()


# In[31]:


df['country'].nunique()


# In[32]:


get_ipython().run_line_magic('pinfo', 'pd.unique')


# In[33]:


df.info()


# In[34]:


df.describe()


# In[35]:


df.describe(include='all')


# In[36]:


df['country'].value_counts()


# In[37]:


df.rename(columns={'country': 'Country'})


# In[38]:


df.rename(columns={'country': 'Country'}, inplace=True)


# In[39]:


df


# In[40]:


df=pd.read_csv('gapminder.csv')


# In[41]:


df


# In[42]:


get_ipython().run_line_magic('pinfo', 'df.rename')


# In[ ]:





# In[43]:


df.drop('continent', axis=1)


# In[44]:


df.drop(columns='continent')


# In[45]:


df.drop(columns=['continent', 'gdp_cap'])


# In[ ]:





# In[46]:


df['new'] = df['life_exp'] + df['gdp_cap']


# In[47]:


df


# In[48]:


df['new1'] = str(df['life_exp']) + df['country'] #this doesnt work


# In[49]:


df.drop(columns='new1', inplace=True)


# In[ ]:





# In[50]:


df['country']


# In[51]:


type(df['country'])


# In[52]:


ser = df['country']


# In[53]:


ser[3]


# In[54]:


ser[3:6]


# In[55]:


ser.index


# In[56]:


ser.index = [i for i in range(2,1706)]


# In[57]:


ser


# In[59]:


# ser[0] ##this will error out


# In[60]:


ser[0:3]


# In[61]:


ser2 = pd.Series(['a', 'b', 'c','d','e','f','g'], index=[1,2,3,4,5,6,7])


# In[62]:


ser2


# In[63]:


ser2[3]


# In[64]:


ser2[2:5] #uses implicit indexing


# In[65]:


ser2[1:4]


# In[66]:


ser3 = pd.Series(['a', 'b', 'c','d','e','f','g'], index=[1.12,2.12,3.12,4.12,5.12,6.12,7.12])
ser3


# In[67]:


ser3 = pd.Series(['a', 'b', 'c','d','e','f','g'], index=['b', 'c','d','e','f','g','a',])
ser3


# In[68]:


ser3[3]


# In[69]:


ser3['e']


# In[70]:


ser3['b':'d']


# In[ ]:





# In[71]:


# loc (always explicit), iloc (always implicit)


# In[72]:


ser2


# In[73]:


ser2.loc[5]


# In[74]:


ser2.loc[4:7] #in case of loc, last index is included unlike list, numpy indexing


# In[76]:


ser3.loc['c':'g'] ## ser3.loc['c':'g'] also works but with loc is suggestible


# In[77]:


ser2.iloc[3]


# In[78]:


ser3


# In[81]:


ser3.iloc[4]


# In[84]:


ser3.iloc[2:7]


# In[86]:


ser3.iloc[2:-1]


# In[89]:


ser3.loc['d':'g']


# In[ ]:




