
# coding: utf-8

# In[1]:


import requests


# In[10]:


response = requests.get("http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm")


# In[11]:


response.encoding = "big5"


# In[12]:


book1 = response.text


# In[14]:


a = book1 [:]


# In[16]:


b = book1 [200:]


# In[18]:


c = book1[:200]


# In[20]:


d = book1[0:200]


# In[22]:


e = book1[0:200:2]


# In[24]:


f = book1[:200:3]


# In[26]:


g = book1[300::3]


# In[28]:


h = book1[::10]

