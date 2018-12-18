import random
import string

a = open("user.txt", "r")
user = input("enter  user name : ").lower()


def pwd():  # Generate Random password
    pawd = string.ascii_letters + string.digits
    return ''.join(random.choice(pawd) for x in range(0, 8))

    # User Verfication

def uname():
    for line in a.readlines():
        b = line.split(":")
        euname = b[0]
        if user == euname:
            present = 1
        else:
            present = 0

    if present == 1:
        print("user name already exists")
    else:
        adduname(user)


# If user is not present add him. Called from Verification function.

def adduname(user):
    a = open("user.txt", "a")
    b = user + ": " + pwd()
    a.writelines(b + "\n")
    print("user registered")


uname()

a.close()
