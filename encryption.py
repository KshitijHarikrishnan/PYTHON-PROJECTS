import string
import random

characters = " " + string.punctuation + string.ascii_letters + string.digits
characters = list(characters) #characters is for real text

replacements = characters.copy() #replacements is for encrypted text
random.shuffle(replacements)

#print(f"chars: {characters}")
#print(f"replacements: {replacements}")



#ENCRYPTION
print("REAL TO ENCRYPTION")
realText = input("Enter a real text: ")
encryptedText = ""

for letter in realText:
    x = characters.index(letter) #x is the position of each letter in the set characters
    encryptedText += replacements[x]
print(f"Real text: {realText}")        
print(f"Encrypted text: {encryptedText}")


print()


#DECRYPTION
print("ENCRYPTION TO REAL")
encryptedText = input("Enter a cipher text: ")
realText = ""

for letter in encryptedText:
    x = replacements.index(letter)
    realText += characters[x]
print(f"Encrypted text: {encryptedText}")    
print(f"Real text: {realText}") 

       
