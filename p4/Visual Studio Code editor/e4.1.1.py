#E-4.1.1: Hello Visual Studio Code

#Problem: Please write a program which asks the user which editor they are using.
# The program should keep on asking until the user types in Visual Studio Code.

#Have a look at the example of expected behaviour below:

        #Editor: Emacs
        #not good
        #Editor: Vim
        #not good
        #Editor: Word
        #awful
        #Editor: Atom
        #not good
        #Editor: Visual Studio Code
        #an excellent choice!

#If the user types in Word or Notepad, the program counters with awful.
#Other unacceptable editor choices receive the reply not good.

#The program should be case-insensitive in its reactions.
#That is, the same user input in lowercase,
#uppercase or mixed case should trigger the same reaction:

#Editor: NOTEPAD
#awful
#Editor: viSUal STudiO cODe
#an excellent choice!

#Solution:

correct_editor = "Visual studio code"

while True:
    check_editor = input("Editor: ")

    if check_editor.lower() == correct_editor.lower():
        print("an excellent choice!")
        break
    elif check_editor.lower() == "word" or check_editor.lower() == "notepad":
        print("awful")
    else:
        print("not good")
