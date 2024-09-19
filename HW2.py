#!/usr/bin/env python
# coding: utf-8

# # STA130 HW Week 2 - Jaeho Yang (yangjae9)

# ### 1. Begin (or restart) part "3(a)" of the TUT Demo and interact with a ChatBot to make sure you understand how each part the Monte Hall problem code above works

# https://chatgpt.com/share/66eb8b00-424c-8007-9f7c-855468270e06

# ### 2. Extend your ChatBot sessions to now address part "3(b)" of the TUT Demo and interact with your ChatBot to see if it can suggest a simpler, more streamlined way to code up this for loop simulation so the process is more clear and easier to understand; then, describe any preferences you have in terms of readibility or explainability between the original code and the code improvements suggested by the ChatBot

# In[7]:


import numpy as np

# Setup
doors = [1, 2, 3]  # List of doors
wins = 0
reps = 100000  # Number of simulations

# Simulation loop
for _ in range(reps):
    winning_door = np.random.choice(doors)  # Randomly select the winning door
    initial_choice = np.random.choice(doors)  # Randomly pick a door

    # Host reveals a "goat" door
    remaining_doors = [door for door in doors if door != initial_choice and door != winning_door]
    goat_door = np.random.choice(remaining_doors)  # Host shows a losing door

    # Switch to the other remaining door
    switch_choice = [door for door in doors if door != initial_choice and door != goat_door][0]

    # Check if switching wins
    if switch_choice == winning_door:
        wins += 1

# Probability of winning by switching
probability = wins / reps
print(probability)


# The difference between the two codes is readability. Since it is a code for the Monty Hall problem, it is good to have variable names that include additional explanations, but personally, I prefer the chatbot's code because the new version of the variable names modified by the chatbot is easier to read.

# ### Break down :

# In[8]:


import numpy as np # import mathematical operations "numpy" generating random choices.


# In[9]:


doors = [1, 2, 3]  # List of doors
wins = 0  # To track how many times switching leads to a win
reps = 100000  # Number of simulations


# doors: You have three doors, one of which has a prize behind it, and the other two have goats (nothing).
# wins: This variable will count how many times switching leads to a win.
# reps: The number of times the simulation will run (100,000 in this case). The more repetitions you have, the more accurate your probability will be.

# In[ ]:


for _ in range(reps):
    winning_door = np.random.choice(doors)  # Randomly select the winning door
    initial_choice = np.random.choice(doors)  # Randomly pick a door


# winning_door: Randomly selects one of the three doors to have the prize behind it.
# initial_choice: Simulates the contestant's first random choice of a door.

# In[ ]:


remaining_doors = [door for door in doors if door != initial_choice and door != winning_door]
goat_door = np.random.choice(remaining_doors)  # Host shows a losing door


# remaining_doors: This list contains the doors that are neither the contestant's initial choice nor the winning door. These are the doors with goats behind them.
# 
# goat_door: The host (who knows which door has the prize) reveals a goat by randomly selecting from the remaining non-winning, non-chosen doors.

# In[ ]:


switch_choice = [door for door in doors if door != initial_choice and door != goat_door][0]


# switch_choice: This simulates the contestant switching doors. The remaining option is the door the contestant switches to.

# In[ ]:


if switch_choice == winning_door:
    wins += 1


# Here, we check if the new choice (after switching) is the winning door. If it is, the wins counter increases.

# In[ ]:


probability = wins / reps
print(probability)


# The probability of winning by switching is simply the number of times switching leads to a win divided by the total number of simulations (reps). This gives an estimate of the success rate of switching.

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo('56mGTszb_iM', width = 550)


# https://chatgpt.com/share/66ec6b4b-58dc-8007-961f-88c2074b1053

# ##### 6. Chatbots are helpful learning tools when learning something new on your own. When I was trying to understand the Monty Hall problem or Markovian ChatBot, I actively used chatbots. The chatbot gave me helpful answers and information to my questions, and I was satisfied with that. However, when I asked a question about the extension to Markovian ChatBot, I had to ask three questions to hear the chatbot's answer. Although my question format did not change, I think it took time to run the code directly or my internet connection may have been the problem, since it gave an appropriate answer on the last attempt. Therefore, the help of the chatbot was helpful for understanding.

# ##### 7. Since I am taking a computer science course, I think that chatbots are effective for learning by understanding coding and using them for new codes, and not unlike my previous thoughts, interacting with chatbots is effective for learning.

# https://chatgpt.com/share/66ec82e2-9dd4-8007-ad2d-c43d6987f015

# In[1]:


print('yes')


# In[ ]:




