'''
ROT 13 is a cypher which you "rotate by 13 places".
A becomes N
N becomes A

Given the name of the exercise "Mod 26", there is a indication that I need to use something with % 26
'''
import string

print(string.ascii_letters)

encoded = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}"
decoded = ""

def decrypt(encodedLetter):
    global decoded
    try:
        decodedLetterIndex = (string.ascii_uppercase.index(encodedLetter) + 13) % 26
        newLetter = string.ascii_uppercase[decodedLetterIndex]
    except ValueError:
        try:
            decodedLetterIndex = (string.ascii_lowercase.index(encodedLetter) + 13) % 26
            newLetter = string.ascii_lowercase[decodedLetterIndex]
        except ValueError:
            newLetter = encodedLetter
    print("----------------")
    decoded = decoded + newLetter
    print(decoded)

for letter in encoded:
    decrypt(letter)

# it will print "picoCTF{next_time_I'll_try_2_rounds_of_rot13_Aphnytiq}"
