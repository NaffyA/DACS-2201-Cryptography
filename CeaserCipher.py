"""
Author: Naffy (Pl4gue) Ahmed
Date: 28th February 2023
Course: DACS2201 - Introduction to Data & Cyber Security @ UDST

Description: Ceaser Cipher Encryptor / Decryptor
"""
def encode_ceaser():
    '''
    plain_text - str
    key - int

    Takes a plain text from the user and the numeric key value to perform shifts to encrypt the message.
    '''
    plaintext = input("Enter text you would like to encrypt: ")
    key = int(input("Enter the key (Number of shifts you want): "))
    cipher_text = ""

    for char in plaintext.upper():
        if char in charset:
            index = charset.find(char) #Finds the index of the character (taken from user) in the characterset (dataset) // returns a Numeric Value.
            new_position = (index + key) % 28 #Index of the character + the key (or # of SHIFTs, taken from the user), gives us the new index of the character in characterset.
#The reason we do % (modulus) is that we have a total of 28 characters, so when it tries to add 28 + 1 key = 29 which is invalid, but with %, for 29 we get 1, technically iterating.
            new_character = charset[new_position] #New_character variable is set to the new_index/position (taken from previous line)
            cipher_text += new_character #Add this to an empty text cipher_text
        else:
            print("{}, this input character not in the character-set. SH*T!".format(char)) #if character not in characterset, display a message

    return cipher_text

def decode_ceaser():
    '''
    cipher_text - str
    key - int

    Takes a cipher text from the user and the numeric key value to perform shifts to get the orginal message back.
    '''
    cipher_text = input("Enter text you would like to decrypt: ") #Get plaintext from user
    key = int(input("Enter the key (Number of shifts you want): ")) #Get key value from user
    decipher = ""
    for char in cipher_text.upper():
        if char in charset:
            index = charset.find(char) 
            new_position = (index - key) % 28 #Here we subtract the index - key, to go back to the original alphabet
            new_character = charset[new_position]
            decipher += new_character
        else:
            print("{}, this input character not in the character-set. SH*T!".format(char)) #if character not in characterset, display a message

    return decipher

## Main ##
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-." #Allowed character-set used for encrypting

print("Welcome to Ceaser Cipher Encryptor / Decryptor")
print("1. Encrypt message using Ceaser Cipher")
print("2. Decrypt Ceaser Cipher")

choice = int(input("Enter your choice: "))
if choice == 1:
    encrypted_text = encode_ceaser()
    print(encrypted_text)
elif choice == 2:
    decrypted_text = decode_ceaser()
    print(decrypted_text)
else:
    print("Program Ending!")
