#E-3.2.5: A line of hashes

#Problem: Please write a program which prints out a line of hash characters,
#the width of which is chosen by the user.

        #Width: 3
        # ###

        #Width: 8
        # ########

#Solution:

width = int(input("Width: "))

print("#"*(width))
