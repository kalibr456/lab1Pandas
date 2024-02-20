#!/usr/bin/env python
# coding: utf-8

# In[62]:


get_ipython().system('pip install matplotlib')
import matplotlib
import pandas as pd
import numpy as np
train = pd.read_csv(r"C:\Users\Gigabyte\Downloads\test.csv")
pd.options.display.expand_frame_repr = False
print("Задание  1")
print(train.head(15))
print(train.shape)
print(train.isnull().sum())
print(train.dtypes)
print("Задание  2")
del train['Cabin']
train['Age'] = train['Age']. fillna(train['Age'].mean())
train['Sex'] = np.where(train['Sex']=="male",0,1)
print(train.head(15))   
    


# In[ ]:





# In[ ]:




