import textwrap
'''
Enter a title (stop to end) => fantastic
fantastic

Found the following title: Fantastic Beasts
Beasts in this title: Ashwinder, Billywig, Bowtruckle, Demiguise,
Diricawl, Doxy, Erumpent, Fwooper, Graphorn, Hippocampus, Lethifold,
Mooncalf, Murtlap, Nundu, Occamy, Runespoor, Swooping Evil, Thestral

Other titles containing beasts in common: Harry Potter and the Cursed
Child, Harry Potter and the Deathly Hallows, Harry Potter and the
Goblet of Fire, Harry Potter and the Order of the Phoenix, the
Wizarding World of Harry Potter

Beasts appearing only in this title: Ashwinder, Billywig, Diricawl,
Graphorn, Lethifold, Mooncalf, Nundu, Occamy, Runespoor, Swooping Evil

Enter a title (stop to end) => phoenix
phoenix

Found the following title: Harry Potter and the Order of the Phoenix
Beasts in this title: Bowtruckle, Doxy, Murtlap, Thestral

Other titles containing beasts in common: Fantastic Beasts

Beasts appearing only in this title:

Enter a title (stop to end) => end
end

This title is not found!

Enter a title (stop to end) => stop
stop
'''
def find_movie (title, names_list):
     '''
     it finds the name of the movie given any part of the movie
     sample input/ output:
     find_movie ('order', ['Order of the', 'Harry Potter','Whaaaaa'])
     (True, 'Order of the')
     '''
     for name in names_list:
          if title.upper() in name.upper():
               return (True, name)
          #makes sure that it can handle parts of words and parts of parts of words
     #need a false return as a tuple because nonetype is not subsctiptable
     return (False,)

def common(dic, title):
     '''
     fids other movies that contain beasts in common
     sample input/ output:
     common({'Fantastic Beasts': {'Runespoor', 'Demiguise', 'Thestral', 'Fwooper', 'Lethifold', 'Graphorn', 'Ashwinder', 'Nundu', 'Doxy', 'Bowtruckle', 'Swooping Evil', 'Murtlap', 'Mooncalf', 'Diricawl', 'Hippocampus', 'Erumpent', 'Occamy', 'Billywig'}, 'Harry Potter and the Order of the Phoenix': {'Bowtruckle', 'Thestral', 'Doxy', 'Murtlap'}, 'Harry Potter and the Cursed Child': {'Demiguise'}}, 'Harry Potter and the Order of the Phoenix')
     (True, 'Fantastic Beasts')
     '''
     movie_list = []
     vals_list = list(dic.values())
     #is a list of sets
     keys_list = list(dic.keys())
     #is a list of names
     for i in range(len(dic)):
          if keys_list[i] != title:
               if dic[title].intersection(vals_list[i]) != set():
               #the set of the intersection of the two sets can't be empty, it may throw the joining off 
                    movie_list.append(keys_list[i])
     return movie_list

def unique_beasts (dic, title):
     '''
     finds beasts only unique to the title movie
     sample input/ output:
     unique_beasts({'Fantastic Beasts': {'Runespoor', 'Demiguise', 'Thestral', 'Fwooper', 'Lethifold', 'Graphorn', 'Ashwinder', 'Nundu', 'Doxy', 'Bowtruckle', 'Swooping Evil', 'Murtlap', 'Mooncalf', 'Diricawl', 'Hippocampus', 'Erumpent', 'Occamy', 'Billywig'}, 'Harry Potter and the Order of the Phoenix': {'Bowtruckle', 'Thestral', 'Doxy', 'Murtlap'}, 'Harry Potter and the Cursed Child': {'Demiguise'}}, 'Harry Potter and the Order of the Phoenix')
     (False,)
     '''
     beast_set = set()
     colation = set()
     vals_list = list(dic.values())
     # is a list of sets of the beasts
     keys_list = list(dic.keys())
     # is a list of names of the movies
     for i in range(len(dic)):
          if keys_list[i] != title:
               for beasts in vals_list[i]:
                    colation.add(beasts)
               diff_set = dic[title] - colation
     return diff_set

def join_wrap_sort(list_, section):
     '''
     factored the print statment,
     creates a string which it then wraps and returns the wrapped 
     list to print out later
     sample input/output:
     join_wrap_sort([Bowtruckle, Doxy, Murtlap, Thestral], 'Beasts in this title')
     Beasts in this title: Bowtruckle, Doxy, Murtlap, Thestral
     '''
     string = ', '.join(sorted(list_))
     string = '{}{}'.format(section,string)
     wrap_list = textwrap.wrap(string)
     return wrap_list     

names_list = []
movies_dict = dict()
hp_file = open('titles.txt')
hp_lines = hp_file.read().split('\n')
names_list = []
for movie in hp_lines:
     beasts = movie.split('|')
     # only the first element of that list is not a beast
     names_list.append(beasts[0])
     movies_dict[beasts[0]]= set()
     for word in range(len(beasts)-1):
          word += 1
          movies_dict[beasts[0]].add(beasts[word])

#at this point movies_dict is dictionary with movies for keys and the values are the movies
#names list is just a list of tuples of names of the movies
true = True
#since i am breaking it when title == stop it should run indefineltly otherwise
title = ''
while true == True:
     title = input('Enter a title (stop to end) => ')
     print(title)
     title = title.upper()
     if title == 'STOP':
          break
     print()
     #If they are both made upper case it keeps uniform when checking against the list

     #part one of code, finds the full name of the movie from input and the beasts from that movie
     if find_movie(title, names_list)[0] == True:
          title = find_movie(title, names_list)[1]

     if title not in movies_dict:
          print('This title is not found!')
          print()
          continue
     else:
          beasts_list = join_wrap_sort(movies_dict[title], 'Beasts in this title: ')
          print('Found the following title: {}'.format(title))
          for line in beasts_list:
               print(line)
     print()

     #part 2 of code, fids other movies that contain beasts in common
     movie_list = common(movies_dict, title)
     match_list_out = join_wrap_sort(movie_list,'Other titles containing beasts in common: ')
     for line in match_list_out:
          print(line)
     print()
     
     # part 3 of code, beasts only unique to this movie
     
     beast_list = unique_beasts (movies_dict, title)
     beast_list_out = join_wrap_sort(beast_list,'Beasts appearing only in this title: ')
     for line in beast_list_out:
          print(line)
     print()
