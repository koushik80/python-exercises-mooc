#E-2.3: Name and address

#Problem:Please write a program which asks for the user's name and address.
#The program should also print out the given information, as follows:

                    #Given name: Steve
                    #Family name: Sanders
                    #Street address: 91 Station Road
                    #City and postal code: London EC05 6AW
                    #Steve Sanders
                    #91 Station Road
                    #London EC05 6AW

#Solution:

name = input("Given name: ")

family_name = input("Family name: ")

s_address = input("Street address: ")

cp_code = input("City and postal code: ")

print(name, family_name)
print(s_address)
print(cp_code)


