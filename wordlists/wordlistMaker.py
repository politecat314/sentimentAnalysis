# -*- coding: utf-8 -*-
"""
Created on Mon May 10 20:23:35 2021

@author: user
"""
# settings
inputName = "negativeWordsRaw.txt"
outputName = "negativeWords.txt"


start = "Negative words"
end = " letter\n"

with open(inputName, encoding='utf-8') as f:
    lines = f.readlines()
    


newlist = []

for index, value in enumerate(lines):
    if value == '\n':
        continue
    
    if str.startswith(value, start) and str.endswith(value, end):
        continue
    
    if str.endswith(value, '\n'):
        newlist.append(value[0:-2])
        
    # print(value)
        
# print(newlist)
final = []

for i in newlist:
    letters = i.split(",")
    
    for j in letters:
        final.append(str.lstrip(j))
            

with open(outputName, 'w') as f:
    for value in final:    
        f.write(str.lower(value) + ',')