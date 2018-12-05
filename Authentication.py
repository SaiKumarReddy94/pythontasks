import random
import string
a=open("user.txt","r")

def pwd():
	pawd=string.ascii_letters + string.digits
	return ''.join(random.choice(pawd) for x in range(0,8))
	
def uname():
	user=input("enter  user name : ")
	for line in a.readlines():
		print(line)
		print("teting")
		b=line.split(":")
		euname=b[0]
		print(euname)
		if user==euname:
			print("user name already exists")
			break
		else:
			adduname(user)

def adduname(user):
	a=open("user.txt","a")
	a.writelines(user+" : "+ pwd())
	print("user registered")

uname()

a.close()
