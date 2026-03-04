Matthew Wilkinson
100434077

HOW TO RUN:
Assuming both server.py and client.py are on turing.uark.edu.
In 2 seperate terminals, run the following commands:
- Terminal 1: python server.py
- Terminal 2: python client.py
Note: You MUST start the server BEFORE the client. So, run
server.py BEFORE client.py

The server will remain running until the ctrl+c interrupt. After
running client.py, the server will report a client has connected.
the client will then need to submit letters to try to guess the 
secret word, which is ARKANSAS. The server will not accept the
client input if it has multiple letters or special characters. 
The server will clean the string submitted if it has only 1
A-Z character with spaces\tabs (for example) and count that as
a guess. The server will send back to the client if the input was
a good guess, terrible guess, or invalid input. The server will
end the game if the user either guesses the word or runs out of 
guesses (7 guesses given at start). After the client disconnects,
another client can connect by running the 'python client.py' 
command.