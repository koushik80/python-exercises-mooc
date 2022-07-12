# E-5.3.5: Phone book, version 2

# Problem: Please write an improved version of the phone book application.
# Each entry should now accommodate multiple phone numbers.
# The application should work otherwise exactly as above,
# but this time all numbers attached to a name should be printed.


# Sample output:

# command (1 search, 2 add, 3 quit): 2
#name: peter
# number: 040-5466745
# ok!
# command(1 search, 2 add, 3 quit): 2
#name: emily
# number: 045-1212344
# ok!
# command(1 search, 2 add, 3 quit): 1
#name: peter
# 040-5466745
# command(1 search, 2 add, 3 quit): 1
#name: mary
# no number
# command(1 search, 2 add, 3 quit): 2
#name: peter
# number: 09-22223333
# ok!
# command(1 search, 2 add, 3 quit): 1
# name: peter
# 040-5466745
# 09-22223333
# command(1 search, 2 add, 3 quit): 3
# quitting...

# Solution:
def phone_book():

    ph_index = {}

    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))

        if command == 1:
            name = input("name: ")
            if name not in ph_index:
                print("no number")
                continue
            for name, numbers in ph_index.items():
                for number in numbers:
                    print(number)

        elif command == 2:
            name = input("name: ")
            number = input("number: ")
            if name not in ph_index:
                ph_index[name] = []
            ph_index[name].append(number)

            print("ok!")

        elif command == 3:
            print("quitting...")
            break

            return ph_index


phone_book()
