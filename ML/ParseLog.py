
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import glob
from sklearn.feature_extraction.text import CountVectorizer


# In[2]:


with open("C:\Learning\Python\ML\LogFiles\Errors2018100112.log") as f:
    array = []
    line2 = ""
    for line in f:
        if (line.startswith("E:") or line.startswith("ERROR:")):
            if (line2!=""):
                if (line2.startswith("ERROR:")):
                    print("Not Insert Java Errors")
                else:
                    array.append(line2.lstrip(" "))
            line2 = line.rstrip("\n")
        else:
            if (line2==""):
                line2 = line.rstrip("\n")
            else:
                line2 = line2+" "+line.rstrip("\n")
    
    if (line2!=""):
        if (line2.startswith("ERROR:")):
            print("Not Insert Java Errors")
        else:
            array.append(line2.lstrip(" "))


# In[3]:


print(len(array))


# In[4]:


headers=[]
for i in range(len(array)):
    words=array[i].split("]")
    array[i]=words[1].lstrip(" ")
    headers.append(words[0])


# In[5]:


for i in range(100):
    print(array[i])
    print(headers[i])


# In[6]:


from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as esw
my_stop_words=["com","eyelit","web","servlet","proxy"]+list(esw)


# In[8]:


vectorizer = CountVectorizer(min_df=1, stop_words=my_stop_words)


# In[9]:


X = vectorizer.fit_transform(array)


# In[10]:


vectorizer.get_feature_names()


# In[11]:


num_samples, num_features = X.shape
print("#Samples: %d, #features: %d" % (num_samples, num_features))


# In[ ]:


X[0]


# In[ ]:


print(X.getrow(0).toarray())


# In[12]:


import scipy as sp


# In[ ]:


v1=X.getrow(0)
v1_norm = v1/sp.linalg.norm(v1.toarray())


# In[ ]:


v1_norm.toarray()


# In[13]:


from sklearn.cluster import KMeans


# In[14]:


num_clusters = 25
km = KMeans(n_clusters=num_clusters, init = 'random', n_init=1, verbose=1)
km.fit(X)


# In[15]:


km.labels_


# In[16]:


for k in range(25):
    indices=(km.labels_==k).nonzero()[0]
    print("***** GROUP %d *************"%(k))
    for i in indices:
        print(headers[i]+array[i])

