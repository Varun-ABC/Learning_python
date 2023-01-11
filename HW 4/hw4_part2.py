'''
Author: Varun Dhir
Purpose: This code runs a loop that asks for commands until the user types in 'end'.
It can find location from a zip code or the zip code(s) of an area from the name of the city and the state 
or it can find the distance from zip to another zip code using the Simplified haversine formula.
Version 1
Final edit: 2/27/19
Sample output:
Command ('loc', 'zip', 'dist', 'end') => loc
loc
Enter a ZIP Code to lookup => 11552
11552
ZIP Code 11552 is in West Hempstead, NY, Nassau county,
coordinates: (040.41'24.90"N,073.39'10.88"W)

Command ('loc', 'zip', 'dist', 'end') => dist
dist
Enter the first ZIP Code => r2903
r2903
Enter the second ZIP Code => 32fw
32fw
The distance between r2903 and 32fw cannot be determined

Command ('loc', 'zip', 'dist', 'end') => zip
zipy
nY
The following ZIP Code(s) found for Troy, NY: 12179, 12180, 12181, 12182, 12183

Command ('loc', 'zip', 'dist', 'end') => eist
eist
Invalid command, ignoring

Command ('loc', 'zip', 'dist', 'end') => dist
dist
Enter the first ZIP Code => 11552
11552
Enter the second ZIP Code => 19459
19459
The distance between 11552 and 19459 cannot be determined

Command ('loc', 'zip', 'dist', 'end') => dist
dist
Enter the first ZIP Code => 11552
11552
Enter the second ZIP Code => 12180
12180
The distance between 11552 and 12180 is 137.08 miles

Command ('loc', 'zip', 'dist', 'end') => end
end

Done
'''
import hw4_util
import math as m

def location_by_zip(zip_codes, zipp):
    '''
    Inputs: a list of lists that contains information on zip codes and an individual zipp code
    Returns a tuple containing, in order, the latitude, longitude, city, state, and county
    Sample output:(42.738678, -73.673862, 'Troy', 'NY', 'Rensselaer')
    '''
    loc_list = []
    for i in zip_codes:
        #'i' runs through the list of lists and i becomes an indivdual list 
        for j in i:
            # 'j' runs through the indivdual list for each city and looks for a match with the zip code
            if j != zipp:
                loc_list.append(1)
                # I want to keep track of how many misses and hits I get   
            elif j == zipp:
                city_idx = zip_codes.index(i)
                info_city = zip_codes[city_idx]
                latitude = info_city[1]
                longitude = info_city[2]
                city = info_city[3]
                state = info_city[4]
                county = info_city[5]
                loc_list.append(5)
    if sum(loc_list) == len(loc_list):
        # because I appended 1 to the list every time it gets a miss and 5 every time it gets a hit, 
        #if it's all misses the length of the list will be equal to the value of it and this branch 
        #will return an empty tuple
        return ()
    else:
        return (latitude, longitude, city, state, county)


def dd_dms(dd_ini):
    '''
    Input: takes a number in decimal digits 
    Returns: The dd number in degrees minuites and seconds without any formatting
    sample output:
    (40,41,24.90)
    '''
    dd = abs(dd_ini)
    deg = int(dd)
    # one degree = 1 whole number
    mins = ((dd - int(dd))*60)
    # takes what's left over from degrees and turns into minutes
    sec = ((mins- m.trunc(mins))*60)
    mins = int(mins)
    return (deg, mins, sec)

def direction(lat, long):
    '''
    input: latitude and longitude
    return: N or S, E or W
    Found it most efficient to call the the decimal digits to DMS twice and this 
    function once as not to copy any code to differenciate between lat and long in the DMS function
    Sample output: (N,W)
    '''
    if lat > 0:
        direc1 = 'N'
    elif lat < 0:
        direc1 = 'S'
    if long > 0:
        direc2 = 'E'
    elif long < 0:
        direc2 = 'W'
    return (direc1,direc2)

        
def zip_by_location(zip_codes, loc):
    '''
    inputs: takes a list of lists of information on cities and a tuple containing 
    the city and state you want to look for
    returns a list of zip codes for the city in the state that the user specified
    sample output: 
    ['12179','12180','12181','12182','12183']
    '''
    zip_list = []
    city = loc[0].lower()
    state= loc[1].lower()
    for i in zip_codes:
        i_lower = [str(ele).lower() for ele in i]
        # I dont want to change the actual list so I create a new list containing only lower case charecters
        for j in i_lower:
            if j == city and i_lower.index(j) == 3 and i_lower[i_lower.index(j)+1]== state:
                #I only want the city to be looked for so the index has to be == 3,
                #if it's anything else it wont count
                zip_list.append(i_lower[0])
    return zip_list

def codes_print(zipps):
    '''
    input: an unknown amount of zip codes as a list
    output, the same zip codes in a way that is formated properly
    sample output: 12180, 12181, 12182, 12183
    '''
    out = ''
    for i in range(len(zipps)):
        if i == len(zipps)-1:
            out += zipps[i]
        else:
            out += zipps[i]+ ', '
    return out

def dist (zip1, zip2):
    '''
    Using the, finds the distance between two points on earth
    input: 2 zip codes
    returns distance as a float
    sample output:
    3783.9056
    '''
    loc1 = location_by_zip(zip_codes, zip1)
    loc2 = location_by_zip(zip_codes, zip2)      
    lat1 = loc1[0]
    long1= loc1[1]
    lat2=loc2[0]
    long2= loc2[1]
    #first I need to get all my data that i will be using, to do so I must call 
    #on another function I wrote previously
    rad_lat1= m.radians(loc1[0])
    rad_long1 = m.radians(loc1[1])
    rad_lat2= m.radians(loc2[0])
    rad_long2 = m.radians(loc2[1])
    radchg_lat = m.radians(lat2 - lat1)
    radchg_long = m.radians(long2 - long1)
    #then I need to convert all my data into radians so that python sin function can output accurate results
    a = m.sin(radchg_lat/2)**2 + m.cos(rad_lat1) * m.cos(rad_lat2) * m.sin(radchg_long/2)**2
    r = 3959.191 
    dist = 2 *r * m.asin(a ** (1/2))
    return dist

if __name__ == "__main__":
    #this makes sure that the body of the code will not be executed when function 
    #are called outside of the program
    zip_codes = hw4_util.read_zip_all()
    com = ''
    i = 0
    while com != 'end':
        i += 1
        com = input("Command ('loc', 'zip', 'dist', 'end') => ")
        print(com)
        com = com.lower()
        
        if com == 'loc':
            zipp = input('Enter a ZIP Code to lookup => ')
            print(zipp)
            if location_by_zip(zip_codes, zipp) == ():
                print('Invalid or unknown ZIP Code\n')
            else:
                info_city = location_by_zip(zip_codes, zipp)
                dms1 = dd_dms(info_city[0])
                dms2 = dd_dms(info_city[1])
                #calls function to turn lat and long from dd into dms  
                nsew = direction(info_city[0], info_city[1])
                print('ZIP Code {} is in {}, {}, {} county,\ncoordinates: ({:03d}\xb0{}\'{:.2f}"{},{:03d}\xb0{}\'{:.2f}"{})\n'\
                      .format(zipp, info_city[2], info_city[3], info_city[4], dms1[0], dms1[1], dms1[2],\
                              nsew[0], dms2[0], dms2[1], dms2[2], nsew[1]))
   
        elif com == 'zip':
            city = input('Enter a city name to lookup => ')
            print(city)
            city= city.lower()
            state = input('Enter the state name to lookup => ')
            print(state)
            state= state.lower()
            loc = (city, state)
            codes = zip_by_location(zip_codes, loc)
            #calls the function and looks up the tuple (city,state) 
            out_codes = codes_print(codes)
            city = city.title()
            state = state.upper()
            if zip_by_location(zip_codes, loc) == []:
                print('No ZIP Code found for {}, {}\n'.format(city, state))
            else:
                print('The following ZIP Code(s) found for {}, {}: {}\n'.format(city, state, out_codes))
        elif com == 'dist':
            first = input('Enter the first ZIP Code => ')
            print(first)
            second = input('Enter the second ZIP Code => ')
            print(second)
            if location_by_zip(zip_codes, first) == () or location_by_zip(zip_codes, second) == ():
                print('The distance between {} and {} cannot be determined\n'.format(first, second))
            else:
                out_dist = dist(first, second)
                print('The distance between {} and {} is {:.2f} miles\n'.format(first,second, out_dist))
        elif com == 'end':
            print('\nDone')
        else:
            print('Invalid command, ignoring\n')