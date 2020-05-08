import sys
#!/usr/bin/env python
# coding: utf-8

# In[19]:
# need to solve problem how to import list file which has miroarray and miRNAseq data( getting error)
# how they need to be lsited? 
# assign the value for Microarray_miRNA_list
MicroArray = X
# assign the value for miRNAseq__miRNA_list
miRNASEQ =  Y
# How to identify if miRNA is present in Microarray_miRNA_list as well as in miRNAseq__miRNA_list when comparing them?
if present in 'X' and 'Y' = Yes
Yes = 2
print("Yes")
if only prenet in 'X' or 'Y' = No
No = 1
print("No")


# In[1]:


get_ipython().run_line_magic('pwd', '')


# In[1]:


import Python_project_data


# In[5]:


import pandas as pd


# In[3]:


pip install pandas


# In[14]:


import pandas as pd
print(pd.__version__)


# In[15]:


import pandas as pd


# In[5]:


import pandas
df1 = pandas.read_excel(open('C:\\Users\\sukik\\project_spring_2020\Python_project_data\MicroArray.xlsx','rb'))
df2 = pandas.read_excel(open('C:\\Users\\sukik\\project_spring_2020\Python_project_data\miRNASEQ.xlsx','rb'))


# In[15]:


df1.head(50)


# In[16]:


df2.head(50)


# In[17]:


df1.tail(50)


# In[18]:


df2.tail(50)


# In[25]:


df1.equals(df2)


# In[26]:


comparison_values = df1.values == df2.values
print (comparison_values)
comparison_values = df1.values == df2.values
print (comparison_values)


# In[26]:


df1.describe()


# In[6]:


df2.describe()


# In[12]:


pd.merge(df1, df2)


# In[40]:


pd.merge(df1, df2, left_index=True, right_index=True)


# In[11]:


import pandas as pd
import pandas
df1 = pandas.read_excel(open('C:\\Users\\sukik\\project_spring_2020\Python_project_data\MicroArray.xlsx','rb'))
df2 = pandas.read_excel(open('C:\\Users\\sukik\\project_spring_2020\Python_project_data\miRNASEQ.xlsx','rb'))


# In[13]:


import matplotlib
print(matplotlib)


# In[23]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[24]:


from matplotlib import pyplot as plt


# In[14]:


import pandas as pd
my_series = pd.Series([8.6, 5.1, -14.0, 3.10])
print(my_series)
from matplotlib import pyplot as plt
plt.plot(my_series)
plt.show()


# In[13]:


import pandas as pd
my_series_1 = pd.Series([4, 6, 2,10, -4, -20, -3, 40])
my_series_2 = pd.Series([14, 16, 12,10, -14, -20, -13, 40])
print(my_series_1)
from matplotlib import pyplot as plt
plt.scatter([my_series_1],[my_series_2])
plt.show()


# In[ ]:

