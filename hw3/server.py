# Matthew Wilkinson
# 100434077

import sys

from socket import *

if sys.argv.__len__() != 2:
    serverPort = 5555
else:
    serverPort = int(sys.argv[1])

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverSocket.bind(('', serverPort))

serverSocket.listen(1)

print("Server is ready to receive")

#game control vars
word = 'arkansas'
guessesLeft = 7
currentIndex = 0

while True:
    connectionSocket, addr = serverSocket.accept()
    print("user connected from ", addr)

    # lets play a game, so keep user connected in a loop
    while True:
        # check end condition
        if guessesLeft <= 0:
            gameEndStr = "\n\nSorry! But you didn't guess the word in time!\nThe word was: ARKANSAS\n\nDisconnecting..."
            connectionSocket.send(gameEndStr.encode('utf-8'))
            break
        
        #lets get the letter
        letter = connectionSocket.recv(1024).decode('utf-8').strip().lower()
        
        # got nothing, assume client left us :(
        if not letter:
            break

        rtnStr = "---\n"
        if len(letter) == 1 and letter.isalpha():
            # is just a letter
            if letter == word[currentIndex]:
                currentIndex += 1
                if currentIndex == len(word):
                    #end game, victory!
                    gameEndStr = "\n\nNice job!!! You guesses all the letters! The word is ARKANSAS\n\nDisconnecting..."
                    connectionSocket.send(gameEndStr.encode('utf-8'))
                    break
                else:
                    rtnStr += "Good guess! %s is in the word! (%i guesses left)" % (letter, guessesLeft) 
            else:
                guessesLeft -= 1
                rtnStr += "Terrible guess! %s isn't in the work! (%i guesses left)" % (letter, guessesLeft)
        else:
            # tell user to just send letter lol
            rtnStr += "Please only send only 1 character\nand make sure its actually a letter."

        connectionSocket.send(rtnStr.encode('utf-8'))

    guessesLeft = 7
    currentIndex = 0
    connectionSocket.close()

    


        
        

            
        
