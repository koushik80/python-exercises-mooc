#E-3.4.6:Chessboard

#Problem: Please write a function named chessboard,
#which prints out a chessboard made out of ones and zeroes.
#The function takes an integer argument,
#which specifies the length of the side of the board.
#See the examples below for details:

        #chessboard(3)
        #print()
        #chessboard(6)

        #101
        #010
        #101

        #101010
        #010101
        #101010
        #010101
        #101010
        #010101

#Solution:

def chessboard(n):
    Sentence_1 = ""
    Sentence_2 = ""
    for i in range(n):
        if i % 2 == 0:
            Sentence_1 += "1"
            Sentence_2 += "0"
        else:
            Sentence_1 += "0"
            Sentence_2 += "1"

    for i in range(n):
        if i % 2 == 0:
            print(Sentence_1)
        else:
            print(Sentence_2)


if __name__ == "__main__":
    chessboard(n)
