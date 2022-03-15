#!/usr/bin/env python
# coding: utf-8

# In[4]:


num = (1, 22, 333, 4444, 55555, 66, 71)
count_odd = 0
count_even = 0
for i in num:
        if not i % 2:
            count_even+=1
        else:
            count_odd+=1
print("num of even numbers :", count_even)
print("num of odd numbers :", count_odd)


# In[ ]:




