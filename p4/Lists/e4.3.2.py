#E4.3.2: Add items to a list

#Problem: Please write a program which first asks the user for the number of items to be added.
#Then the program should ask for the given number of values, one by one,
#and add them to a list in the order they were typed in. Finally, the list is printed out.

#An example of expected behaviour:


#Sample output:

        #How many items: 3
        #Item 1: 10
        #Item 2: 250
        #Item 3: 34
        #[10, 250, 34]


#NB: this exercise doesn't ask you to write any functions,
#so you should not place any code within an if __name__ == "__main__" block.

#Solution:

i = 0
list = []
num = int(input("How many items: "))

while i < num:
    value = int(input(f'Item {i}:'))
    i += 1
    list.append(value)
print(list)
