#E-4.9: Students in groups

#Problem: Please write a program which asks for the number of students on a course and the desired group size.
#The program will then print out the number of groups formed from the students on the course.
#If the division is not even, one of the groups may have fewer members than specified.

#If you can't get your code working as expected,
#it is absolutely okay to move on and come back to this exercise later.
#The topic of the next section is conditional statements.
#This exercise can also be solved using a conditional construction.

            #How many students on the course? 8
            #Desired group size? 4
            #Number of groups formed: 2

            #How many students on the course? 11
            #Desired group size? 3
            #Number of groups formed: 4


#Solution:

num_students = int(input("How many students on the course?"))
size_groups = int(input("Desired group size?"))

group_form = (num_students + size_groups - 1) // size_groups

print("Number of groups formed:", group_form)

