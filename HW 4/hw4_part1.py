import hw4_util
lists_count = hw4_util.get_number_of_password_lists()
file = input("Select the list of common passwords by entering a number between 0 and {} => ".format(lists_count-1))
print(file)
file = int(file)
pas = input("Enter a password => ") 
#pas short for password
print(pas)
len_pas = len(pas)
list_pas = list(pas)
rules_list = []
# this list will help me find which rules weren't satified and which were
#this is rule 1
if (len_pas <= 25 and len_pas >= 4) and 'A'<= list_pas[0] <= 'z':
    print('Rule 1 is satisfied')
    rules_list.append(1)
else:
    print('Rule 1 is not satisfied')
    rules_list.append(0)

#put rule 2 here
lists_count = hw4_util.get_number_of_password_lists()
idx = 0
rule2_list = []
#this list will help me keep track of if the password was in the file of passwords
file_list = hw4_util.get_password_list(file)
while idx < len(file_list):
    if file_list[idx] == pas:
        rule2_list.append(1)
    else:
        rule2_list.append(0)
    idx += 1 
if sum(rule2_list) > 0:
    print('Rule 2 is not satisfied')
    rules_list.append(0)
else:
    print('Rule 2 is satisfied')
    rules_list.append(1)
# this is rule 3 
if (list_pas.count('@') >= 1 or list_pas.count('$') >= 1)and list_pas.count('%') == 0:
    print('Rule 3 is satisfied')
    #checks the count of each of the forbidden symbols
    rules_list.append(1)
else:
    print('Rule 3 is not satisfied')
    rules_list.append(0)

#this is rule 4
if (pas.upper() != pas and pas.lower() != pas) or list_pas.count('1') > 0 or list_pas.count('2') > 0 or list_pas.count('3') > 0 or\
   list_pas.count('4'):
    #first part sees if the password all upper case/ lowercase is the same as the normal password- meaning that the password is
    #all lower/upper case, the second part checks the count of 1,2,3,4
    print('Rule 4 is satisfied')
    rules_list.append(1)
else:
    print('Rule 4 is not satisfied')
    rules_list.append(0)
#this is rule 5
i = 0
rule5_list = []
#this list helps me keep track if every time theres a capital letter that theres a _ following it
rule5_list2 = []
#this list helps me know if the last letter is capital
while i <= (len_pas-2):
    if (list_pas[i] < 'a' and list_pas[i+1] == '_'):
        rule5_list2.append(1)
        if list_pas[len_pas-1] >= 'a':
            rule5_list.append(1)
    else:
        rule5_list.append(0)
    i += 1
if sum(rule5_list) == len(rule5_list) or len(rule5_list2) == 0:
    print('Rule 5 is satisfied')
    rules_list.append(1)
else: 
    print('Rule 5 is not satisfied')
    rules_list.append(0)
#this is rule 6
if list_pas.count('5') > 0 or list_pas.count('6') > 0 or list_pas.count('7') > 0 or\
   list_pas.count('8') > 0 or list_pas.count('9') > 0 or list_pas.count('0') > 0:
    print('Rule 6 is not satisfied')
    rules_list.append(0)
else:
    print('Rule 6 is satisfied')
    rules_list.append(1)
    
if sum(rules_list) == len(rules_list):
    print('The password is valid')

elif rules_list[0] == 1:
    if len(pas) >= 6:
        newpas = 'A suggested password is: {}{}{}42{}{}{}'.format(list_pas[0],list_pas[1],list_pas[2],list_pas[-3],list_pas[-2],list_pas[-1])
        #a splice of the first and last 3 elements of the password list with 42 added inbetween
        print(newpas)
else:
    print('The password is not valid')