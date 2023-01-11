import json
'''
Author: Varun Dhir
version 1
purpose look through a dictionary of movie information from IMDB with the movie id as a key 
and another dictionary of the information as the values and a dictionary  
of twitter reviews that has a movie id as keys and a list of reviews as the value
the code computes the average value of the the reviews based on user input weight 
and looks through the dictionary for movies that match user inputs
such as min and max year and genre
it then out puts the best and worst movie based on average reviews for the input years
sample output:

Min year => 2000
2000
Max year => 2016
2016
Weight for IMDB => 0.7
0.7
Weight for Twitter => 0.3
0.3

What genre do you want to see? sci-fi
sci-fi

Best:
        Released in 2014, Interstellar has a rating of 8.70

Worst:
        Released in 2015, Fantastic Four has a rating of 4.72

What genre do you want to see? drame
drame

No Drame movie found in 2000 through 2016

What genre do you want to see? drama
drama

Best:
        Released in , The Dark Knight has a rating of 9.20

Worst:
        Released in 2012, Spring Breakers has a rating of 4.91

What genre do you want to see? stop
stop
'''

def calc_avg (w1, w2, num1, num2):
    '''
    calcultes the weihted average of two numbers
    sample output: 2.01
    '''
    return (w1* num1 + w2 * num2) / (w1+w2)

def find_review_movie (movies_dict, twit_dict, gene, min_yr, max_yr, w_imdb, w_twit):
    '''
    main chunk of code for this hw
    takes the movies dictionary, the twitter reviews dictionary, the genre, the min and max years, and the weights
    it creates a listof tuples that fit all the specifications, i.e are in the year range, have more then 3 twitter reviews,
    and are in the requested genre
    it outputs the average (calls the calc_avg function) the name of the movie and the year it was released as a tuple
    sample output:
    [(8.580000000000002, 'The Butterfly Effect', 2004), (8.286666666666667, 'Donnie Darko', 2001), (8.186666666666667, '28 Days Later...', 2002),\
    (7.540000000000001, 'Planet of the Apes', 2001), (7.140000000000001, 'Minority Report', 2002)]
    '''
    avg_movie = []
    for movie in movies_dict:
        if movie in twit_dict:
            twitter = twit_dict[movie]
            if len(twitter) < 3:
                continue
            ind_mov = movies_dict[movie]
            # so far Ive checked that the movie is in the IMDB dictionary, 
            #the Twitter dictionary, and has more than three reviews on Twitter
            g_list = ind_mov['genre']
            for g in range(len(g_list)):
                g_list[g] = g_list[g].lower()
            if gene.lower() in g_list:
                #now I have the genre too
                if ind_mov['movie_year'] <= max_yr and ind_mov['movie_year'] >= min_yr:
                    #now I will see if the movie is in the right grouping of years
                    #after all that is done I am ready to calculate the average rating
                    avg_r = calc_avg(w_imdb,w_twit, ind_mov['rating'], sum(twitter)/len(twitter))
                    avg_movie.append((avg_r, ind_mov['name'], ind_mov['movie_year']))
    return sorted(avg_movie, reverse = True)

if __name__ == "__main__":
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())
    min_yr = input('Min year => ')
    print(min_yr)
    min_yr = int(min_yr.strip())
    max_yr  = input('Max year => ')
    print(max_yr)
    max_yr = int(max_yr.strip())
    w_imdb = input('Weight for IMDB => ')
    print(w_imdb)
    w_imdb = float(w_imdb.strip())
    w_twit = input('Weight for Twitter => ')
    print(w_twit)
    w_twit = float(w_twit.strip())
    print()
    while True:
        gene_og = input('What genre do you want to see? ')
        print(gene_og)
        gene = gene_og.lower().strip()
        if gene == 'stop':
            break
        print()
        rt_nm_yr = find_review_movie (movies, ratings, gene, min_yr, max_yr, w_imdb, w_twit)
        #an orderes list of tuples with the rating, name and year for each movie that fits all specifications
        if rt_nm_yr != []:
            best = rt_nm_yr[0]
            worst = rt_nm_yr[len(rt_nm_yr)-1]
            #since the list is sorted in the function all i have to do is take the first and last elements
            print('Best:')
            print('\t\tReleased in {}, {} has a rating of {:.2f}'.format(best[2],best[1],best[0]))
            print()
            print('Worst:')
            print('\t\tReleased in {}, {} has a rating of {:.2f}'.format(worst[2],worst[1],worst[0]))
        else:
            print('No {} movie found in {} through {}'.format(gene_og.title(), min_yr, max_yr))
        print()