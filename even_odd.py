try:
    n = int(input("enter you number:"))

    if(n==0):
         print("the number is zero")
    elif(n % 2 ==0):
        print("the number is even")       
    else:
        print("the number is odd") 

except ValueError:
      print("please enter a valid number")

#if we give a string like "abc" then python shows value error 
# because int() converts strings into an integern  
