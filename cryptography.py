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
    addlist = []

    
    if command=="e":
        message = input("Message: ")
        key = input("Key: ")
        
        for x in message:
            mlist.append(associations.find(x))
        for x in key:
            klist.append(associations.find(x))
        
        n = len(mlist)
        while n>0:
            y = klist[len(mlist)-n]
            klist.append(y)
            n=n-1
        
        ziplist = list(zip(klist, mlist))
        for x in ziplist:
            addlist.append(x[0] + x[1])
        
        for x in addlist:
            if x<= len(associations):
                print(associations[x], end="")
            else:
                print(associations[x-len(associations)-1], end="")
        print( )
    
    
    
    elif command=="d":
        message = input("Message: ")
        key = input("Key: ")
        
        
    
    
    else: 
        print("Did not understand command, try again.")
    
    command = input("Enter e to encrypt, d to decrypt, or q to quit: ")

if command=="q":
    print("Goodbye!")