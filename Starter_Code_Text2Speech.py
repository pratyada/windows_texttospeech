
# coding: utf-8

# # Lets make the text "SPEAK"

# In[11]:


from gtts import gTTS 
import os


# In[63]:


import easygui
location = easygui.fileopenbox()
file = open(location, "r").read().replace("\n", " ")


# In[33]:


#file = open("text1.txt", "r").read().replace("\n", " ")


# In[64]:


language = 'en'


# In[65]:


speech = gTTS(text = str(file), lang = language, slow = False)


# In[66]:


speech.save("voice.mp3")


# In[67]:


os.system("start voice.mp3")


# In[ ]:


print("press enter to finish")


# In[ ]:


#the end

