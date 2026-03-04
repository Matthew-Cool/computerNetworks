# Matthew Wilkinson
# 100434077

import sys

from socket import *

if sys.argv.__len__() != 3:
    serverName = 'localhost'
    serverPort = 5555
else:
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

print('Lets play hangman! The word has 8 letters!\n')

while True:
    letter = input("Input a letter: ")
    snd = letter.encode('utf-8')
    clientSocket.send(snd)

    response = clientSocket.recv(1024).decode('utf-8')
    if 'Nice' in response or 'Sorry' in response:
        print(response)
        break
    print(response)

clientSocket.close()

