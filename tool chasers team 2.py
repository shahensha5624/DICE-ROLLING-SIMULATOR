#!/usr/bin/env python
# coding: utf-8

# In[20]:


#Rolling the dice
import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    print(random.randint(min, max))
    print(random.randint(min, max))

    roll_again =("Roll the dices again?")
print(roll_again)
print(roll_again)


# In[21]:


import random
roll_dice = input("Write start to dice roll: ")

if roll_dice == "start":
   posiblle_results = [1, 2, 3, 4, 5, 6]
   result = random.choice(posiblle_results)
   print("Result of dice rolling is : " + str(result))


# In[13]:


import random
roll_dice = input("Write start to dice roll: ")

if roll_dice == "start":
   posiblle_results = [1, 2, 3, 4, 5, 6]
   result = random.choice(posiblle_results)
   print("Result of dice rolling is : " + str(result))


# In[ ]:





# In[ ]:




