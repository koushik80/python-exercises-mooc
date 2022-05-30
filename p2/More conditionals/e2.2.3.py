#E-2.2.3:The elder

#Problem: Please write a program which asks for the names and ages of two persons.
#The program should then print out the name of the elder.

#Some examples of expected behaviour:

        #Person 1:
        #Name: Alan
        #Age: 26
        #Person 2:
        #Name: Ada
        #Age: 27
        #The elder is Ada

        #Person 1:
        #Name: Bill
        #Age: 1
        #Person 2:
        #Name: Jean
        #Age: 1
        #Bill and Jean are the same age

#Solution:

print("Person 1:")
n_1 = input("Name: ")
a_1 = int(input("Age: "))

print("Person 2:")
n_2 = input("Name: ")
a_2 = int(input("Age: "))

if a_1 > a_2:
    print(f"The elder is {n_1}")
elif a_1 < a_2:
    print(f"The elder is {n_2}")
else:
    print(f"{n_1} and {n_2} are the same age")
