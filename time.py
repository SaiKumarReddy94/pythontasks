# a=input("enter time in 12 hour Standard in hh:mm:ss AM/PM   format ")
# print(a)
# def t(a):
# 	time= a
# 	if time[-2:]=="AM" and time[:2]== 12:
# 		return("00"+time[2:-2])
# 	elif time[-2:]=="AM":
# 		return(time[:-2])
# 	elif time[-2:]=='PM' and time[:2]==12:
# 		return(time[-2:])
# 	else:
# 		return(str(time[:2]+12)+str(time[2:8])	
# print(t('a'))



# Python program to convert time 
# from 12 hour to 24 hour format 
  
# Function to convert the date format 
def convert24(str1): 
      
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2] 
          
    # remove the AM     
    elif str1[-2:] == "AM": 
        return str1[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        print(str1[:2])
        return str(int(str1[:1]) + 12) + str(str1[1:8]) 
  
# Driver Code  
str2=input("input time")       
print(convert24(str2)) 
