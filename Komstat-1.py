#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import numpy as np
import pyreadstat as ps


# In[11]:


df, meta = ps.read_sav("D:/KOMSTAT/Pert2/komstat1.sav")


# In[119]:


df.head(50)


# In[15]:


df.shape


# In[70]:


df.columns


# In[117]:


df.dtypes


# In[118]:


df.info()


# In[121]:


df.isna().sum()


# In[49]:


df[df["Name"].duplicated(keep=False)]


# In[64]:


df.describe()


# In[71]:


df.groupby('Position').aggregate(['min', np.median,np.mean, max])


# In[189]:


df[df.Market_value == df.Market_value.max()]


# In[190]:


df[df.Market_value == df.Market_value.min()]


# In[191]:


df[df.Age == df.Age.max()]


# In[192]:


df[df.Age == df.Age.min()]


# In[79]:


import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[85]:


df["Position"].value_counts()


# In[107]:


df['Position'].value_counts().plot.bar()
plt.tight_layout()


# In[125]:


df['Age'].value_counts().plot.bar(color='g')
plt.tight_layout()
plt.show()


# In[178]:


df["League_from" ].value_counts().head(10).plot.barh()
plt.tight_layout()
plt.show()


# In[173]:


df["League_to"].value_counts().head(10).plot.barh()
plt.tight_layout()
plt.show()

