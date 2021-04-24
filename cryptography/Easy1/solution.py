At first I didn't know what to do

But reading the task twice, I noticed the words 'flag', 'key' and 'table'

So I googled 'cryptography message key table' and looking at the images I stumbled accross the same table as I was given

To my surprise I discovered the name of this crypto by accident LOL. It's called a 'Vigenère cipher'

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

That's how it works. Now I need to develop a python script to cypher and decypher Vigenère cipher
