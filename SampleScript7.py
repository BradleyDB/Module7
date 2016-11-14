
#--Data--#

User_Num=None#This gets the value from the user
show_user=None#This is the display variable

#--Processing--#

def display():
    while(True):#Help the user out by giving them more than once change
        try:#start of the block where you test your code
            User_Num=int(input("Please type an Number: "))#asking for input
            break #if int is found we move on to assigning the name_value variable
        except ValueError: #if anything but an int is input I print an error message instead of having my code break
            print("Please try again with a numeral e.g '5' or '256'")#the new 'error message'
    show_user=User_Num
    return show_user

#--I/O--#

print(display())
