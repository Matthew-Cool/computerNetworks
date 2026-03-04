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
word = 'ARKANSAS'
guessWord = list('________')
guessedLetters = ''
guessesLeft = 7
charLeft = 8

def lettersReplace(let):
    global charLeft, guessWord, word

    i = 0
    for char in word:
        if let == char:
            guessWord[i] = let
            charLeft -= 1
        i += 1

while True:
    connectionSocket, addr = serverSocket.accept()
    print("user connected from ", addr)

    initStr = 'Lets play hangman! The word has %i letters!\n%s\n\n' % (len(word), "".join(guessWord))
    connectionSocket.send(initStr.encode('utf-8'))

    # lets play a game, so keep user connected in a loop
    while True:
        
        #lets get the letter
        #maybe try catch block so if client disconnects it doesn't crash server...?
        try: 
            letter = connectionSocket.recv(1024).decode('utf-8').strip().upper()
        except:
            print("Error receiving from client. Client probably disconnected.")
        
        # got nothing, assume client left us :(
        if not letter:
            print("Didn't get value from client, so the client (%s) must've disconnected by accident." % (str(addr)))
            break

        rtnStr = ""
        if len(letter) == 1 and letter.isalpha() and letter not in guessedLetters:
            # is just a letter
            guessedLetters += letter
            if letter in word:
                lettersReplace(letter)
                if charLeft <= 0:
                    gameEndStr = "\n\nNice job!!! You guesses all the letters!\nThe word is ARKANSAS\n\nDisconnecting..."
                    connectionSocket.send(gameEndStr.encode('utf-8'))
                    break
                else: 
                    rtnStr += "Good guess! %s is in the word! (%i guesses left)\n%s" % (letter, guessesLeft, "".join(guessWord)) 
            else:
                guessesLeft -= 1
                # check end condition
                if guessesLeft <= 0:
                    gameEndStr = "\n\nSorry! But you didn't guess the word in time!\nThe word was: ARKANSAS\n\nDisconnecting..."
                    connectionSocket.send(gameEndStr.encode('utf-8'))
                    break
                else:
                    rtnStr += "Terrible guess! %s isn't in the word! (%i guesses left)\n%s" % (letter, guessesLeft, "".join(guessWord))
        else:
            # tell user to just send letter lol
            if letter in guessedLetters:
                rtnStr += "You've already guessed this letter! Please try a different letter."
            else:
                rtnStr += "Please only send only 1 character\nand make sure its actually a letter."

        rtnStr += "\n\n"
        connectionSocket.send(rtnStr.encode('utf-8'))

    guessesLeft = 7
    charLeft = 8
    guessedLetters = ''
    guessWord = list('________')    
    connectionSocket.close()
    print('client %s has disconnected, waiting for new player...' % (str(addr)))

    


        
        

            
        
