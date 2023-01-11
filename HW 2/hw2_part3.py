'''
Part 3: Happy/ sad sentence
CS1 

Author: Varun Dhir
Date: 2/13/19
Version 1.0

Sample output: 

Enter a sentence => why is the "excellent" car riddled with so many problems, I hate it
why is the "excellent" car riddled with so many problems, I hate it
Sentiment: +--
This is a sad sentence.
'''
inisent = input ('Enter a sentence => ')
print(inisent)
inisent = inisent.lower()
def number_happy(sen):
    happy = sen.count('laugh')+ sen.count('happiness') + sen.count('love') + sen.count('excellent') + sen.count('good') + sen.count('smile')
    return happy
#created a function that counts all of the happy words
def number_sad(sen):
    sad= sen.count('bad')+ sen.count('sad') + sen.count('terrible') + sen.count('horrible') + sen.count('problem') + sen.count('hate')
    return sad
#ditto for sad words
print("Sentiment: ", number_happy(inisent)* '+', number_sad(inisent) * '-', sep = '')
if number_happy(inisent)> number_sad(inisent):
    print ('This is a happy sentence.')
    #compares happy and sad words
elif number_sad(inisent)> number_happy(inisent):
    print ('This is a sad sentence.')
    #ditto 
else:
    print('This is a neutral sentence.')