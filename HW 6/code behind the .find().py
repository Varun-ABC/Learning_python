# maybe use is subset and a list of sets instead of lists (but then order is messed up)?
## use.find() for this part 
# and if true then run through the list of tuples of full movie names
#and see if the order is right for the individual title list  
title_list = title.split()
title_set = set(title_list)
#title_set = [x.upper for ele in title_set] 
print(title_set)
#the tuple is the name of the movie spilt up ex: ('Fantastic','Beasts') 
for tpl_idx in range(len(names_list)):
     
     name_set = set(names_list[tpl_idx])
     print(name_set)
     name_set = set(ele.upper() for ele in name_set)
     print(name_set)
     if title_set <= name_set:
          
          print(len(names_list[tpl_idx])-1, '18')
          for word_idx in range(len(names_list[tpl_idx])-1):
               word = names_list[tpl_idx][word_idx]
               word = word.upper()
               print(word, '22')
               next_word = names_list[tpl_idx][word_idx+1].upper()
               print(next_word, '24')
               print(word_idx, '25')
               for title_idx in range(len(title_list)-1):
                    if word == title_list[title_idx] and next_word == title_list[title_idx+1]:
                         full_movie = ' '.join(names_list[tpl_idx])
                         return (True,full_movie)
                    #sooooooo close works if the first two words are valid and the third isn't