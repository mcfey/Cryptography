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
    mlist = []
    klist = []
    endlist = []
    
    if command=="e":
        message = input("Message: ")
        key = input("Key: ")
        
        for x in message:
            mlist.append(associations.find(x))
        for x in key:
            klist.append(associations.find(x))
        
        print(mlist)
        print(klist)
        
        n = len(mlist)
        while n>0:
            y = klist[len(mlist)-n]
            klist.append(y)
            n=n-1
        
        print(klist)
        
        ziplist = list(zip(klist, mlist))
        
        for x in ziplist:
            endlist.append(x[0] + x[1])
        
        print(endlist)
    
    elif command=="d":
        message = input("Message: ")
        key = input("Key: ")
        print("e")
        
    
    else: 
        print("Did not understand command, try again.")
    
    command = input("Enter e to encrypt, d to decrypt, or q to quit: ")

if command=="q":
    print("Goodbye!")