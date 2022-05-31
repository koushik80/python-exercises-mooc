#E-2.3.6:Alphabetically in the middle

#Problem:Please write a program which asks the user for three letters.
#The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

#You may assume the letters will be either all uppercase, or all lowercase.

#Some examples of expected behaviour:

        #1st letter: x
        #2nd letter: c
        #3rd letter: p
        #The letter in the middle is p

        #1st letter: C
        #2nd letter: B
        #3rd letter: A
        #The letter in the middle is B

#Solution:

L1 = input("1st letter:")
L2 = input("2nd letter:")
L3 = input("3rd letter:")


if L1 > L2 and L1 > L3:
    if L2 > L3:
        ml = L2
    else:
        ml = L3
elif L2 > L3:
    if L3 > L1:
        ml = L3
    else:
        ml = L1
elif L2 > L1:
    ml = L2
else:
    ml = L1

print("The letter in the middle is", ml)
