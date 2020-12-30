#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np


# In[ ]:


Question:1
get_ipython().set_next_input('Convert a 1D array to a 2D array with 2 rows');get_ipython().run_line_magic('pinfo', 'rows')
Desired output::
array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])


# In[26]:


a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a.reshape(2,5)


# In[ ]:


Question:2
get_ipython().set_next_input('How to stack two arrays vertically');get_ipython().run_line_magic('pinfo', 'vertically')
Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])


# In[29]:


arr1 = np.array([[0, 1, 2, 3, 4] , [5, 6, 7, 8, 9]])

arr2 = np.array([[1, 1, 1, 1, 1] , [1, 1, 1, 1, 1]])

arr = np.vstack((arr1, arr2))

print(arr)


# In[ ]:


Question:3
get_ipython().set_next_input('How to stack two arrays horizontally');get_ipython().run_line_magic('pinfo', 'horizontally')
Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])


# In[33]:


arr1 = np.array([[0, 1, 2, 3, 4] , [5, 6, 7, 8, 9]])

arr2 = np.array([[1, 1, 1, 1, 1] , [1, 1, 1, 1, 1]])

arr = np.hstack((arr1, arr2))

print(arr)


# In[ ]:


Question:4
get_ipython().set_next_input('How to convert an array of arrays into a flat 1d array');get_ipython().run_line_magic('pinfo', 'array')
Desired Output::
        array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# In[41]:


f = np.array([[0,1,2,3,4], [5,6,7,8,9,]])
x = f.reshape(-1)
print(x)


# In[ ]:


Question:5
get_ipython().set_next_input('How to Convert higher dimension into one dimension');get_ipython().run_line_magic('pinfo', 'dimension')
Desired Output::
        array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])


# In[49]:


f = np.array([[[0,1,2,3,4,], [5,6,7,8,9] , [10,11,12,13,14]]])
x = f.reshape(-1)
print(x)


# In[ ]:


Question:6
get_ipython().set_next_input('Convert one dimension to higher dimension');get_ipython().run_line_magic('pinfo', 'dimension')
Desired Output::
        array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])


# In[51]:


f = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
x = f.reshape(5,3)
print(x)


# In[ ]:


Question:7
get_ipython().set_next_input('Create 5x5 an array and find the square of an array');get_ipython().run_line_magic('pinfo', 'array')


# In[62]:


a = np.random.randn(5,5)
a


# In[69]:


np.square(a)


# In[ ]:


Question:8
get_ipython().set_next_input('Create 5x6 an array and find the mean');get_ipython().run_line_magic('pinfo', 'mean')


# In[70]:


a = np.random.randn(5,6)
a


# In[71]:


a.mean()


# In[ ]:


Question:9
get_ipython().set_next_input('Find the standard deviation of the previous array in Q8');get_ipython().run_line_magic('pinfo', 'Q8')


# In[73]:


a.std()


# In[ ]:


Question:10
get_ipython().set_next_input('Find the median of the previous array in Q8');get_ipython().run_line_magic('pinfo', 'Q8')


# In[75]:


np.median(a)


# In[ ]:


Question:11
get_ipython().set_next_input('Find the transpose of the previous array in Q8');get_ipython().run_line_magic('pinfo', 'Q8')


# In[78]:


a.T


# In[ ]:


Question:12
get_ipython().set_next_input('Create a 4x4 an array and find the sum of diagonal elements');get_ipython().run_line_magic('pinfo', 'elements')


# In[81]:


a = np.random.randn(4,4)
a


# In[82]:


np.trace(a)


# In[ ]:


Question:13
get_ipython().set_next_input('Find the determinant of the previous array in Q12');get_ipython().run_line_magic('pinfo', 'Q12')


# In[88]:


det =  np.linalg.det(a)
det


# In[ ]:


Question:14
get_ipython().set_next_input('Find the 5th and 95th percentile of an array');get_ipython().run_line_magic('pinfo', 'array')


# In[98]:


np.percentile(a, 5)


# In[99]:


np.percentile(a, 95)


# In[ ]:


Question:15
get_ipython().set_next_input('How to find if a given array has any null values');get_ipython().run_line_magic('pinfo', 'values')


# In[92]:


a = np.random.randn(2,2)
a


# In[100]:


np.isnan(a)

