import random
import string

a = open("user.txt", "r")

def pwd():              #Generate Random password
    pawd = string.ascii_letters + string.digits
    return ''.join(random.choice(pawd) for x in range(0, 8))
    
        #User Verfication

def uname():
    user = input("enter  user name : ")
    for line in a.readlines():
        b = line.split(":")
        euname = b[0]
        if user == euname:
            print("user name already exists")
            break
        else:
            adduname(user)
            break
            
#If user is not present add him. Called from Verification function.

def adduname(user):
    a = open("user.txt", "a")
    b= user + " : " + pwd()
    a.writelines(b + "\n")
    print("user registered")


uname()

a.close()
