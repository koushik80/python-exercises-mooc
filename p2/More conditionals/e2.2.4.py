#E-2.2.4:Alphabetically last

#Problem:Python comparison operators can also be used on strings.
#String a is smaller than string b if it comes alphabetically before b.
#Notice however that the comparison is only reliable if

    #the characters compared are of the same case, i.e. both UPPERCASE or both lowercase
    #only the standard English alphabet of a to z, or A to Z, is used.

#Please write a program which asks the user for two words.
#The program should then print out whichever of the two comes alphabetically last.

#You can assume all words will be typed in lowercase entirely.

#Some examples of expected behaviour:

        #Please type in the 1st word: car
        #Please type in the 2nd word: scooter
        #scooter comes alphabetically last.

        #Please type in the 1st word: zorro
        #Please type in the 2nd word: batman
        #zorro comes alphabetically last.

        #Please type in the 1st word: python
        #Please type in the 2nd word: python
        #You gave the same word twice.

#Solution:

w_1 = input("Please type in the 1st word: ")
w_2 = input("Please type in the 2nd word: ")

if w_1 < w_2:
    print(f"{w_2} comes alphabetically last.")
elif w_1 > w_2:
    print(f"{w_1} comes alphabetically last.")
else:
    print("You gave the same word twice.")
