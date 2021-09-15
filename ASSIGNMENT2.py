#!/usr/bin/env python
# coding: utf-8

# In[25]:


#1Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)

s=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
max=[]
for x in s:
    max.append(x[-1])
l=sorted(max)
print(l)
new_list=[]
for i in range(len(l)):
    for x in s:
        if l[i]==x[-1]:
            new_list.append(x)
print(new_list)


# In[21]:


#2.Assignment(2)Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values
s={}
for x in range (ord("a"),ord("z")+1):
    s[chr(x)]=x
print(s)


# In[ ]:




