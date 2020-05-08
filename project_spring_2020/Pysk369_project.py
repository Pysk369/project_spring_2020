#!/usr/bin/env python
# coding: utf-8

# In[19]:


Fold_change = 2
print(Fold_change)


# In[24]:


Fold_change = 4 + 4
print("Fold_change")


# In[26]:


KO_change = 4
print(KO_change)


# In[27]:


ratio_fold = Fold_change / KO_change
print('ratio_fold')


# In[28]:


type(Fold_change)


# In[29]:


type(KO_change)


# In[30]:


type(ratio_fold)


# In[31]:


print(4/2)


# In[32]:


print(2/4)


# In[33]:


print (2*4)


# In[34]:


print(2+4)


# In[39]:


WT_miRNA320a = 5.28
KO_miRNA320a = 26.4
# HOW KO large than WT, when comparing them?
Difference = WT_miRNA320a - KO_miRNA320a * 100
print("fold difference = " , Difference, "?")


# In[41]:


WT_miRNA320a = 26.4
KO_miRNA320a = 5.28
# HOW KO large than WT, when comparing them?
Difference = WT_miRNA320a / KO_miRNA320a * 100
print("fold difference = " , Difference, "?")


# In[42]:


WT_miRNA320a = 5.28
KO_miRNA320a = 26.4
# HOW KO large than WT, when comparing them?
Difference = WT_miRNA320a / KO_miRNA320a * 100
print("fold difference = " , Difference, "?")


# In[43]:


WT_miRNA320a = 5.28
KO_miRNA320a = 26.4
# HOW KO large than WT, when comparing them?
Difference = WT_miRNA320a - KO_miRNA320a / 100
print("fold difference = " , Difference, "?")


# In[44]:


WT_miRNA320a = 5.28
KO_miRNA320a = 26.4
# HOW KO large than WT, when comparing them?
Difference = WT_miRNA320a + KO_miRNA320a * 100
print("fold difference = " , Difference, "?")


# In[45]:


WT_miRNA320a = 5.28
KO_miRNA320a = 26.4
# HOW KO large than WT, when comparing them?
Difference = WT_miRNA320a + KO_miRNA320a / 100
print("fold difference = " , Difference, "?")


# In[46]:


print(min(18, 6, 498, 4, 53, 5, 4, 165, 1, 77, 11, 4, 461, 5, 143, 87, 6, 16, 2, 17, 29, 14, 13, 11, 70, 73, 19, 2548, 578))
print(max(18, 6, 498, 4, 53, 5, 4, 165, 1, 77, 11, 4, 461, 5, 143, 87, 6, 16, 2, 17, 29, 14, 13, 11, 70, 73, 19, 2548, 578))


# In[47]:


print(abs(32))


# In[12]:


list(range(12))


# In[11]:


nums = range(16)
print(type(nums))


# In[9]:


range(start, stop, step)
# Create a new list of odd numbers from 1 to 31 by unpacking a range object
nums_list2 = [*range(3,32,6)]
print(nums_list2)


# In[48]:


print(abs(-32))


# In[10]:


# Convert nums to a list
nums_list = list(nums)
print(nums_list)


# In[49]:


print(float(17))
print(int(1.67))
# they can be called  on strings
print(int('2548') + 1)


# In[16]:


print(" I have learnt some basic python code from instructor John Lee_ spring biof309")
print(" great! and iniate real project")


# In[ ]:


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




