#!/usr/bin/env python
# coding: utf-8

# In[28]:


#email_id = ankit@gmail.com
#Password = '1234'
email_id = input('Enter your name : ')
if '@' in email_id:
    Password = input('Enter your Password : ')
    #pass
    if (email_id == 'ankit@gmail.com') & (Password == '1234'):
            print('Welcome')
    elif (email_id == 'ankit@gmail.com') & (Password != '1234'):
        print('Please conrrect your password')
        Password = input('Enter your Password : ')
        if Password == '1234':
            print('All ok to go')
        else:
                print('Still Password is wrong')
    else:
            print('Incorrect credentials')
else:
    print('Please enter correct E-mail ')


# In[ ]:




