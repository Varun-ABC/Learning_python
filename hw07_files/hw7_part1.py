'''
Author: Varun Dhir
Date: 4/20/19
version 1
purpose: using a dictionary of words that include given values for frequency of word usage
the auotcorrect first checks if the input word is in the dictionary as is
if it is then nothing else is done
if it not then it tries a series of functions on it- first it will try to drop one or two letters from 
anywhere in the word and try to match it then weather or not there was a match previously it will pass the input through 
the swap function that swaps two letters in the orignal word and looks for match, so on for replace which replaces each 
letter of the input with letters that are close to the original letter on a key board and insert which inserts a letter at all 
positions in the input word. 
from the returns of each of these funtions, the top three (or more if there is a tie), in terms of frequency are printed

Sample Output:
Dictionary file => words_10percent.txt
words_10percent.txt
Input file => input_words.txt
input_words.txt
Keyboard file => keyboard.txt
keyboard.txt
barely          -> barely          :FOUND
carats          -> carats          :FOUND
confabs         -> confabs         :FOUND
corepulent      -> corpulent       :MATCH 1
costumye        -> costumey        :MATCH 1
pamek           -> pamek           :NO MATCH
darjed          -> darned          :MATCH 1
darjed          -> dared           :MATCH 2
darjed          -> darked          :MATCH 3
doitd           -> doit            :MATCH 1
doitd           -> doits           :MATCH 2
dovrtailing     -> dovetailing     :MATCH 1
flavoonls       -> flavonols       :MATCH 1
outstpend       -> outspend        :MATCH 1
hut             -> shut            :MATCH 1
hut             -> jut             :MATCH 2
pashas          -> pashas          :FOUND
poolry          -> poorly          :MATCH 1
poolry          -> poly            :MATCH 2
quixmasters     -> quizmasters     :MATCH 1
relocatiing     -> relocating      :MATCH 1
sorceresd       -> sorceress       :MATCH 1
turbulences     -> turbulences     :FOUND
sut             -> shut            :MATCH 1
inteters        -> inters          :MATCH 1
inteters        -> integers        :MATCH 2
marteatment     -> marteatment     :NO MATCH
agew            -> ages            :MATCH 1
agew            -> agee            :MATCH 2
agew            -> anew            :MATCH 3
shu             -> shut            :MATCH 1
shu             -> shy             :MATCH 2
shu             -> shh             :MATCH 3
'''

def drop (set_d, word):
    '''
    drops a letter in the input and checks if it is in the dictionary file
    if it is not in the file it returns False if it is in the file it returns True and 
    a set of all the matches
    sample input/ output
    drop({'this', 'is', 'my','dictionary','hiss'}, 'thiss')
    (True,{this, 'hiss'})
    '''
    multi_set = set()
    word_list = list(word)
    for i in range(len(word_list)):
        newword_list = word_list.copy()
        #this has to be inside the for loop so that it resets every time
        newword_list[i] = ''
        #puts a blank spot in the list where the letter we want to remove is   
        new_word =''.join(newword_list)
        if new_word in set_d:
            multi_set.add(new_word)
        nw_list2 = list(new_word)
        for j in range(len(nw_list2)):
            newword_list2 = nw_list2.copy()
            newword_list2[j] = ''
            new_word2 =''.join(newword_list2)
            if new_word2 in set_d:
                multi_set.add(new_word2)
    if  multi_set != set():
        multi_set = sorted(multi_set)
        return (True, multi_set)
    else:
        return (False,)
    #my return needs to be subscriptable so I needed to make it a one element tuple

def swap(set_d, word):
    '''
    takes two conscutive values in the input word and swaps them 
    then checks if it is the dictionary
    sample input/ output:
    swap({'this', 'is', 'my','dictionary'}, 'ym')
    (True,{'my'})
    '''
    multi_set = set()
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
            multi_set.add(new_word)
    if multi_set != []:
        multi_set = sorted(multi_set)
        return (True, multi_set)
    else:
        return (False,)

    
def replace(set_d, word, keyboard):
    '''
    uses a dictionary of the qwerty key board with single letters as keys and a set of the letters agasent to the letter
    as the values to replace a letter in the input with each letter from alphabet
    if the new word exists in the dictionary then it puts in a list and only returns the
    all mathces
    sample input/ output:
    replace({'this', 'is', 'my','dictionary'}, 'dictionzry', {'a':{'q','w','s','z'}, 'z': {'x','s','a'}})
    (True,{'dictionary'})
    '''
    multi_set = set()
    word_list = list(word)
    for i in range(len(word_list)):
        for j in keyboard[word_list[i]]:
            newword_list = word_list.copy()
            # Needs to refresh the list every single ideration
            #atleast once per spot in list so that it doesn't replace it more than once
            newword_list[i] = j
            new_word =''.join(newword_list)
            if new_word in set_d:
                multi_set.add(new_word)
    if multi_set != []:
        multi_set = sorted(multi_set)
        return (True, multi_set)
    else:
        return (False,)
    
def insert(set_d, word):
    '''
    using a list of letters inserts every letter in every postion and looks for a match
    with the set of words
    if theres a match then adds it to a set 
    the funtion returns a tuple if the set is empty and retuns True and the set of matches
    insert({'this', 'is', 'my','dictionary', 'dictionryt'}, 'dictionry')
    (True,{'dictionary','dictionryt'})
    '''
    multi_set = set()
    letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'\
    ,'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'\
    ,'w', 'x', 'y', 'z']
    word_list = list(word)
    for i in range(len(word_list)+1):
        for lt in letters:
            word_list = list(word)
            word_list.insert(i,lt)
            #word_list[i] = lt
            new_word = ''.join(word_list)
            if new_word in set_d:
                multi_set.add(new_word)

    if multi_set != []:
        multi_set = sorted(multi_set)
        return (True, multi_set)
    else:
        return (False,)    

dict_file = input('Dictionary file => ')
print(dict_file)
dict_file = dict_file.strip()
#dict_file = 'words_10percent.txt' #just for testing

words_file = input('Input file => ')
print(words_file)
words_file = words_file.strip()

#words_file = 'input_words.txt' #just for testing

key_file = input('Keyboard file => ')
print(key_file)
key_file = key_file.strip()
#key_file = 'keyboard.txt' #just for testing

dict_file = open(dict_file)
words_file = open(words_file)
key_file = open(key_file)

dict_lines = dict_file.read()
dict_set = set(dict_lines.split('\n'))
dict_set.remove('')


just_words = set()
#set (to be) of just the words
words_f = dict()
#dictionary (to be) with words as keys and freq as values

for wf in dict_set:
    wf_list = wf.split(',')
    just_words.add(wf_list[0])
    words_f[wf_list[0]] = wf_list[1]

word_lines = words_file.read()
words_list = word_lines.split('\n')
if '' in words_list:
    words_list.remove('')

key_lines = key_file.read()
key_list = key_lines.split('\n')
if '' in key_list:
    key_list.remove('')
key_dict = dict()
#dictionary with the letter as a key and all adjacent letters as values

for lst in key_list:
    key_dict[lst[0]] = lst[1:]

for word in words_list:
    match_list = []
    # a to be list of tuples where the first ele is the freq and the sec is the word
    word= word.strip()
    if word in just_words and not word[0].isdigit():
        autoc = 'FOUND'
        print('{:<14} -> {:<14} :{}'.format(word,word,autoc))
        continue
    if drop(just_words, word)[0] == True:
        # Why I needed an else return to also be a tuple so that it can be subscriptable
        multi_list = drop(just_words, word)[1]
        match_list += multi_list
        # i add the return list to the match_list so that its not multiple lists just one long list with all the returns
    if insert(just_words, word)[0] == True:
        multi_list = insert(just_words, word)[1]
        match_list += multi_list
        
    if swap(just_words,word)[0] == True:
        multi_list = swap(just_words, word)[1]
        match_list += multi_list
        
    if replace(just_words, word, key_dict)[0] == True:
        multi_list = replace(just_words, word, key_dict)[1]
        match_list += multi_list
    if match_list == []:
        new_word = word
        autoc = 'NO MATCH'
        print('{:<14} -> {:<14} :{}'.format(word,new_word, autoc))
        continue
    
    for wrd in range(len(match_list)):
        match_list[wrd] = (words_f[match_list[wrd]],match_list[wrd])
        #makes the match list into list of tuples with the frequency as the
        #first element and the the second element being the word
    match_set = set(match_list)         
    match_set = sorted(match_set,reverse=True)
    rank = 1
    runs = 1
    for it in range(len(match_set)):
        f_wd = match_set[it]
        freq = f_wd[0] 
        wd = f_wd[1]
        print('{:<14} -> {:<14} :MATCH {}'.format(word,wd,rank))
        rank += 1
        if it != len(match_set)-1:
            if match_set[it+1][0] != freq:
                #only increase runs when the next word doesn't have the same 
                #freq as the last one 
                runs += 1
        if runs == 4:
            break
        