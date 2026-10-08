import string

def atbash_cipher(text):
    alphabet = string.ascii_uppercase
    reversed_alphabet = alphabet[::-1]
    
    trans_table = str.maketrans(
        alphabet + alphabet.lower(), 
        reversed_alphabet + reversed_alphabet.lower()
    )
    
    return text.translate(trans_table)

user_input = input("Enter text: ")
print(atbash_cipher(user_input))