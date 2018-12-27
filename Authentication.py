import random
import string
a = open("user.txt", "r")

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def pwd():  # Generate Random password
    pawd = string.ascii_letters + string.digits
    return ''.join(random.choice(pawd) for x in range(0, 8))

    # If user is not present add him. Called from Verification function.

def adduname(user):
    a.close()
    c = open("user.txt", "a")
    b = user + ": " + pwd()+ "\n"
    c.writelines(b)
    print(user + " user registered")
    c.close()


        # User Verfication

def uname():
    user = input("enter  user name : ").lower()
    tmp=1
    if a.readline()=="":
        print("db empty")
        tmp=0
    else:
        for line in a.readlines():
            print(line)
            b = line.strip().split(":")
            euname = b[0]
            if user == euname:
                tmp = 1
                #a.close()
                break
            else:
                tmp = 0
    print(tmp)
    if tmp == 1:
        print("user name already exists")
        a.close()
    else:
        adduname(user)

uname()


#############################################################################################################################
###########################################################################################################################
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
