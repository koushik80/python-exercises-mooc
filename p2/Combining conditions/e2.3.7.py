#E-2.3.7:Gift tax calculator

#Explanation:Some say paying taxes makes Finns happy,
#so let's see if the secret of happiness lies in one of the taxes set out in Finnish tax code.

#According to the Finnish Tax Administration,
#a gift is a transfer of property to another person against no compensation or payment.
#If the total value of the gifts you receive from the same donor in the course of 3 years is €5,000 or more, you must pay gift tax.

#When the gift is received from a close relative or a family member,
#the amount of tax to be paid is determined by the following table, which is also available on this website:

            #Value of gift              Tax at the        Tax rate for the
                                       #lower limit      #exceeding part(%)

            #5000 — 25000	               100	                  8
            #25000 — 55000	               1700	                  10
            #55000 — 200000	               4700	                  12
            #200000 — 1000000	           22100	              15
            #1000000 —	                   142100	              17

#So, for a gift of 6 000 euros the recipient pays a tax of 180 euros (100 + (6 000 - 5 000) * 0.08).
#Similarly, for a gift of 75 000 euros the recipient pays a tax of 7 100 euros (4 700 + (75 000 - 55 000) * 0.12).

#Problem: Please write a program which calculates the correct amount of tax for a gift from a close relative.
#Have a look at the examples below to see what is expected.
#Notice the lack of thousands separators in the input values
#- you may assume there will be no spaces or other thousands separators in the numbers in the input,
#as we haven't yet covered dealing with these.

            #Value of gift: 3500
            #No tax!

            #Value of gift: 5000
            #Amount of tax: 100.0 euros

            #Value of gift: 27500
            #Amount of tax: 1950.0 euros

#Solution:

value = int(input("Value of gift: "))

x = 5000
tax_lr_limit = 0
tax_r_excd = 0

tax = (tax_lr_limit + (value - x) * tax_r_excd)

if value < x:
    print("No tax!")
elif value >= x:
    if tax_lr_limit >= 100 and tax_r_excd >= 8:
        print("Amount of tax:",tax,"euros")
    else:
        False



####undone