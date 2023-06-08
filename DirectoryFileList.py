#!/usr/bin/env python
# coding: utf-8

# In[20]:


# import OS module
import os

# Set Directory to Iterate Through
path = "C:\\Users\\avisb\\iCloudDrive\\Audiobooks"

# Create list of File Objects 
files = os.listdir(path)

# Start building output 
output = f"Files and directories in {path}:\n\n"
i = 1 

# Iterate through list of files and print file name to new line 
for file in files: 
    output += f"{i}. {file}\n"
    i+= 1

# Write output to a file in local directory 
f = open("FilesList.txt", "w")
f.write(output)
f.close()


# In[ ]:




