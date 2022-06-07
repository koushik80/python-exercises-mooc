#E-3.2.6:A rectangle of hashes

#Problem: Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

        #Width: 10
        #Height: 3
        ##########
        ##########
        ##########

#Solution:

w = int(input("Width: "))
h = int(input("Height: "))

for i in range(h):
    print('#'*(w))
