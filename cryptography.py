"""
cryptography.py
Author: Mary Feyrer
Credit: Tess Snyder

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

command = input("Enter e to encrypt, d to decrypt, or q to quit: ")


while command!="q":
    output = []
    keylist = []
    
    if command=="d":
        message = input("Message: ")
        key = input("Key: ")
        
        for x in message:
            output.append(associations.find(x))
        for x in key:
            keylist.append(associations.find(x))
            
    print(output) print(key)
    
    elif command=="e":
        message = input("Message: ")
        key = input("Key: ")
        print("e")
    
    else: 
        print("Did not understand command, try again.")
    
    command = input("Enter e to encrypt, d to decrypt, or q to quit: ")

if command=="q":
        print("Goodbye!")