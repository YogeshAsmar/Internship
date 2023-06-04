#!/usr/bin/env python
# coding: utf-8

# ## Internship Task 4
# 
# Write a Python program using NumPy to perform the following tasks on a given array:
# 1. Create a NumPy array with the following values: [1, 2, 3, 4, 5].
# 2. Print the shape of the array using the .shape attribute.
# 3. Reshape the array into a 2D array with 2 rows and 3 columns.
# 4. Print the shape of the new array.
# 5. Create a second NumPy array with the following values: [6, 7, 8, 9, 10].
# 6. Concatenate the two arrays together horizontally.
# 7. Print the resulting array.
# 8. Compute the resulting array's mean, median, and standard deviation.

# In[1]:


import numpy as np


# In[2]:


a = np.array([1,2,3,4,5]) ##Create a NumPy array with the following values: [1, 2, 3, 4, 5].


# In[3]:


np.shape(a) ##Print the shape of the array using the .shape attribute


# We cannot reshape array with 5 elements into (2,3) format son we will add zero as 6th element in our previous array

# In[4]:


a1 = np.array([0,1,2,3,4,5])


# In[5]:


a2 = np.reshape(a1,(2,3)) ##Reshape the array into a 2D array with 2 rows and 3 columns


# In[6]:


print(a2)


# In[7]:


print(a2.shape) ##Print the shape of the new array


# In[8]:


b1 = np.array([6,7,8,9,10]) ##Create a second NumPy array with the following values: [6, 7, 8, 9, 10]


# In[9]:


c1 = np.concatenate((a1,b1),axis = 0) ##Concatenate the two arrays together horizontally


# In[10]:


print(c1) ##Print the resulting array


# In[11]:


np.mean(c1) ## Mean


# In[12]:


np.median(c1) ##Median


# In[13]:


np.std(c1) ##Standard Deviation


# In[ ]:




