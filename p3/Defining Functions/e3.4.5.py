#E-3.4.5:A square of hashes

#Problem:Please write a function named hash_square(length),
#which takes an integer argument.
#The function prints out a square of hash characters,
#and the argument specifies the length of the side of the square.

        #hash_square(3)
        #print()
        #hash_square(5)
#Sample output:

        ###
        ###
        ###

        #####
        #####
        #####
        #####
        #####

#Solution:

def hash_square(length):
    for i in range(1, length+1):
        if i > 0:
            print(length * "#")

    print()


if __name__ == "__main__":
    hash_square(5)
