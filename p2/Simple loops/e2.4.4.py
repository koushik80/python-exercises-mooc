#E-2.4.4:

#Problem: Please write a program which asks the user for a password.
#The program should then ask the user to type in the password again.
#If the user types in something else than the first password,
#the program should keep on asking until the user types the first password again correctly.

#Have a look at the expected behaviour below:

        #Password: sekred
        #Repeat password: secret
        #They do not match!
        #Repeat password: cantremember
        #They do not match!
        #Repeat password: sekred
        #User account created!




#Solution 2:
#password = input("Password: ")
#repeat_password = input("Repeat password: ")
#while True:
    #password = " sekred"
    #if repeat_password == " sekred":
        #print("User account created!")
        #break
    #else:
        #print("They do not match!")
        #repeat_password = input("Repeat password: ")

#Solution2:

password1 = input("Password: ")
while True:
    password2 = input("Repeat password: ")
    if password1 != password2:
        print("They do not match!")
    else:
        print("User account created!")
        break
