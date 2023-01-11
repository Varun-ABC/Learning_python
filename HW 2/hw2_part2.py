'''
Part 2: cipher
CS1 

Author: Varun Dhir
Date: 2/13/19
Version 1.0

Sample output

Enter a string to encode ==> y so Serius?
y so Serius? 

Encrypted as ==> *%$ s7654 S2(*2(ri@@@s?
Difference in length ==> 11
Deciphered as ==> y so Serius?
Operation is reversible on the string.
'''
def encrypt(word):
    word= word.replace(' a', '%4%')
    word= word.replace('he','7!')
    word= word.replace('e', '9(*9(')
    word= word.replace('y', '*%$')
    word= word.replace('u','@@@')
    word= word.replace('an','-?')
    word= word.replace('th', '!@+3')
    word= word.replace('o', '7654')
    word= word.replace('9','2')
    word= word.replace('ck','%4')
    return word
#chain replacement so it goes down the list
def decrypt (word):
    word= word.replace('%4','ck')    
    word= word.replace('2','9')
    word= word.replace('7654', 'o')
    word= word.replace('!@+3', 'th')
    word= word.replace('-?','an')
    word= word.replace('@@@','u')
    word= word.replace('*%$', 'y')
    word= word.replace ('9(*9(', 'e')
    word= word.replace('7!','he')
    word= word.replace('%4%', ' a')
    return word
#have to reverese the first func so that the stuff in (...) is reversed and the gen order is reveresed 
cipher = input ("Enter a string to encode ==> ")
print (cipher, "\n")
out_1 = "Encrypted as ==> {}". format(encrypt(cipher))
print(out_1)
diff_ = len((encrypt(cipher)))- len(cipher)
out_2 = 'Difference in length ==> {}'.format(diff_)
print(out_2)
out_3 = 'Deciphered as ==> {}'.format(decrypt(encrypt(cipher)))
print(out_3)
if decrypt(encrypt(cipher)) == cipher :
    print('Operation is reversible on the string.')
else:
    print('Operation is not reversible on the string.')