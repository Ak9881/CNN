#!/usr/bin/env python
# coding: utf-8

# In[8]:


a = int(input('Enter number which table you want to see..'))

i=1

while i<11:
    print(a,'*',i, a*i)
    i+=1
    
    


# # Guessing Game

# In[12]:


import random 
random.randint(1,100)


# In[19]:


Lucky_draw = random.randint(1,100)#1 number ahe
Guess = int(input('Guess the number : '))#2 ra number milala ata ty dohana compare kraychy

counter = 1

while Guess != Lucky_draw:# Ashi condition takaychi ki jo pryat apli condition statify nahi hot to pryat loop madhech
    print('Congratuations you Win..!!!')
    if Guess>Lucky_draw:
        print('Guess the Lower number')
    else:
        print('Guess the Higher number')
        
    Guess = int(input('Guess the number : '))
    counter+=1
print('Congratuations you Win..!!!')
print('You took', counter,'attempts')
        
    


# In[ ]:





# In[ ]:




