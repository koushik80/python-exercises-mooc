#E-2.4.5: PIN and number of attempts

#Problem: Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321.
#The program should then print out the number of times the user tried different codes.

        #PIN: 3245
        #Wrong
        #PIN: 1234
        #Wrong
        #PIN: 0000
        #Wrong
        #PIN: 4321
        #Correct! It took you 4 attempts

#If the user gets it right on the first try, the program should print out something a bit different:

        #PIN: 4321
        #Correct! It only took you one single attempt!


#Solution:

attempt = 0

while True:
    code = input("PIN:")
    attempt += 1

    if code == "4321":
        success = True
        break

    elif code != "4321":
        success = False
        print("Wrong")


if attempt == 1:
    success = True
    print(f"Correct! It only took you one single attempt!")
elif attempt > 1:
    success = True
    print(f"Correct! It took you {attempt} attempts")
