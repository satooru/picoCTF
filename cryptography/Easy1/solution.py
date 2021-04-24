'''
At first I didn't know what to do

But reading the task twice, I noticed the words 'flag', 'key' and 'table'

So I googled 'cryptography message key table' and looking at the images I stumbled accross the same table as I was given

To my surprise I discovered the name of this crypto by accident LOL. It's called a 'Vigenere cipher'

The way it works is:
    - given the message 'MESSAGE'
    - and the key 'KEY'

You repeat the key until it matches the message's length like this: 'KEYKEYK'

Then you match:
    - the letter from the message with the row
    - the letter from the key with column

So in our example:
    - message:    'MESSAGE'
    - key:        'KEYKEYK'
    - cyphertext: 'WIQCEEO'

That's how it works. Now I need to develop a python script to cypher and decypher Vigenere cipher
'''
import string

print(string.ascii_uppercase)

decoded = ""
key     = "SOLVECRYPTO"
encoded = "UFJKXQZQUNB"

# I expect to append a string with a decoded letter
def decrypt(key, encoded):
    print("---------------")
    global decoded
    print("key " + key)
    print("encoded " + encoded)
    # I realized the first letter for the key always starts with itself so that means the key shifts the alphabet
    column = string.ascii_uppercase.index(key)
    print("column " + str(column))
    # it means that when I have the encoded letter I'd shift according to the key (or column)
    row = string.ascii_uppercase.index(encoded) - column
    print("row " + str(row))
    decoded = decoded + string.ascii_uppercase[row]
    print(decoded)

for i in range(len(encoded)):
    decrypt(key[i], encoded[i])

# at the end it prints "CRYPTOISFUN"
