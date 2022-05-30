#E-2.1.3:Typecasting

#Problem:Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately.
#Use the Python int function.

#You can assume the number given by the user is always greater than zero.

#An example of expected behaviour:

        #Please type in a number: 1.34
        #Integer part: 1
        #Decimal part: 0.34

#Solution:


num = float(input("Please type in a number:"))

int_num = int(num)
dec_num = num % 1

print(f"Integer part: {int_num}")
print(f"Decimal part: {dec_num}")
