#E4.3.3: Addition and removal

#Problem: Please write a program which asks the user to choose between addition and removal.
#Depending on the choice, the program adds an item to or removes an item from the end of a list.
#The item that is added must always be one greater than the last item in the list.
#The first item to be added must be 1.

#The list is printed out in the beginning and after each operation.
#Have a look at the example execution below:


#Sample output:

        #The list is now []
        #a(d)d, (r)emove or e(x)it: d
        #The list is now [1]
        #a(d)d, (r)emove or e(x)it: d
        #The list is now [1, 2]
        #a(d)d, (r)emove or e(x)it: d
        #The list is now [1, 2, 3]
        #a(d)d, (r)emove or e(x)it: r
        #The list is now [1, 2]
        #a(d)d, (r)emove or e(x)it: d
        #The list is now [1, 2, 3]
        #a(d)d, (r)emove or e(x)it: x
        #Bye!

#You may assume that, if the list is empty, there will not be an attempt to remove items.

#NB: this exercise doesn't ask you to write any functions,
#so you should not place any code within an if __name__ == "__main__" block.

#Solution:

list = []
i = 1

while True:
    print(f'The list is now {list}')
    choice = input(f'a(d)d, (r)emove or e(x)it:')
    if choice == "d":
        list.append(i)
        i += 1
    elif choice == "r" :
        list.pop(len(list) - 1)
        i -= 1
    elif choice == "x":
        break
print("Bye!")
