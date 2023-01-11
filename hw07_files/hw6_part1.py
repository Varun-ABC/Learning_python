'''
Author: Varun Dhir
version 1
AutoCorrect
purpose: takes two files: one of input words and another with a dictionary 
of words and first tries to find the word in the dictionary. If that doesm't
work it drops each letter letter from the input if one of those 'words' is in the dictionary
it stores it, if none of the droped 'words'are in the dictionary then it will try to swap 
consecutive letters in the input if one of the iterations are a match it stores it in a list
If swap doesn't work it goes to replacing a single letter from the input with a hardcodded list 
the alphabet, it still doesn't work then there is no match.
sample output:

Dictionary file => part1/words_all_i.txt
part1/words_all_i.txt
Input file => part1/input_words3.txt
part1/input_words3.txt
abacus         -> abacas         :REPLACE
a              -> a              :NO MATCH
suckcessfull   -> suckcessfull   :NO MATCH
k              -> k              :NO MATCH
rr             -> ar             :REPLACE
klm            -> elm            :REPLACE
intrinsick     -> intrinsic      :DROP
you            -> you            :FOUND
'''

dict_file = input('Dictionary file => ')
print(dict_file)
words_file = input('Input file => ')
print(words_file)
dict_file = open(dict_file)
words_file = open(words_file)

dict_lines = dict_file.read()
dict_set = set(dict_lines.split('\n'))
dict_set.remove('')

word_lines = words_file.read()
words_list = word_lines.split('\n')
if '' in words_list:
    words_list.remove('')

def drop (set_d, word):
    '''
    drops a letter in the input and checks if it is in the dictionary file
    if it is not in the file it returns False if it is in the file it returns True and the word as a tuple
    sample input/ output
    drop({'this', 'is', 'my','dictionary'}, 'thiss')
    (True,'this')
    '''
    multi_list = []
    word_list = list(word)
    for i in range(len(word_list)):
        newword_list = word_list.copy()
        #this has to be inside the for loop so that it resets every time
        newword_list[i] = ''
        #puts a blank spot in the list where the letter we want to remove is   
        new_word =''.join(newword_list)        
        if new_word in set_d:
            multi_list.append(new_word)
    if  multi_list != []:
        #cant do min on an empty list
        new_word = min(multi_list)
        return (True, new_word)
    else:
        return (False,)
    #my return needs to be subscriptable so I needed to make it a one element tuple

def swap(set_d, word):
    '''
    takes two conscutive values in the input word and swaps them 
    then checks if it is the dictionary
    sample input/ output:
    swap({'this', 'is', 'my','dictionary'}, 'ym')
    (True,'my')
    '''
    multi_list = []
    word_list = list(word)
    for i in range(len(word_list)-1):
        #since the last letter has nothing to be swapped with we will 
        #iterate until the second to last letter 
        newword_list = word_list.copy()
        letter2 = newword_list[i]
        #i need to store the value of first letter we are swapping before i 
        #do the swap because the value will change in the next step 
        newword_list[i] = newword_list[i+1]
        newword_list[i+1] = letter2
        new_word =''.join(newword_list)
        if new_word in set_d:
            multi_list.append(new_word)
    if multi_list != []:
        new_word = min(multi_list)
        return (True, new_word)
    else:
        return (False,)

def replace(set_d, word):
    '''
    uses a list of letters to replace a letter in the input with each letter from alphabet
    if the new word exists in the dictionary then it puts in a list and only returns the
    smallest value lexographically
    sample input/ output:
    replace({'this', 'is', 'my','dictionary'}, 'dictionzry')
    (True,'dictionary')
    '''
    multi_list = []
    letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'\
    ,'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'\
    ,'w', 'x', 'y', 'z']
    word_list = list(word)

    for i in range(len(word_list)):
        for j in letters:
            newword_list = word_list.copy()
            # Needs to refresh the list every single ideration, atleast once per spot in list so that it doesn't replace it more than once or 
            newword_list[i] = j
            new_word =''.join(newword_list)
            if new_word in set_d:
                multi_list.append(new_word)
    if multi_list != []:
        new_word = min(multi_list)
        return (True, new_word)
    else:
        return (False,)

for word in words_list:
    if word in dict_set:
        autoc = 'FOUND'
        print('{:<14} -> {:<14} :{}'.format(word,word,autoc))
        continue
    elif drop(dict_set, word)[0] == True:
        # Why I needed an else return to also be a tuple so that it can be subscriptable
        tpl = drop(dict_set, word)
        new_word = tpl[1]
        autoc = 'DROP'
    elif swap(dict_set,word)[0] == True:
        new_word = swap(dict_set, word)[1]
        autoc = 'SWAP'
    elif replace(dict_set, word)[0] == True:
        new_word = replace(dict_set, word)[1]
        autoc = 'REPLACE'
    else:
        new_word = word
        autoc = 'NO MATCH'
    print('{:<14} -> {:<14} :{}'.format(word,new_word,autoc))