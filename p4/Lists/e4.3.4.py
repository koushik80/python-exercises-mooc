#E4.3.4: Same word twice

#Problem:Please write a program which asks the user for words.
#If the user types in a word for the second time,
#the program should print out the number of different words typed in, and exit.


#Sample output:

        #Word: once
        #Word: upon
        #Word: a
        #Word: time
        #Word: upon
        #You typed in 4 different words

#NB: this exercise doesn't ask you to write any functions,
#so you should not place any code within an if __name__ == "__main__" block.

#Solution

lst = []

while True:
    w = input("Word: ")
    if w in lst:
        break
    lst.append(w)
print(f'You typed in {len(lst)} different words')




#different method:

#lst = []
#i = 0

#while True:
    #w = input("Word: ")

    #if w in lst:
        #print(f'You typed in {i} different words')
        #break
    #else:
        #lst.append(w)
        #i += 1
