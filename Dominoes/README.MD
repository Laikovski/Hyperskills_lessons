## Stage 1/5: Setting Up the Game 

    - Generate a full domino set. Each domino is represented as a list of two numbers. A full domino set is a list of 28 unique dominoes.
    - Split the full domino set between the players and the stock by random. You should get three parts: Stock pieces (14 domino elements), Computer pieces (7 domino elements), and Player pieces (7 domino elements).
    - Determine the starting piece and the first player. Modify the parts accordingly. You should get four parts with domino pieces and one string indicating the player that goes first: either "player" or "computer"

## Stage 2/5: The Interface
    
    - Print the header using seventy equal sign characters (=).
    - Print the number of dominoes remaining in the stock – Stock size: [number].
    - Print the number of dominoes the computer has – Computer pieces: [number].
    - Print the domino snake. At this stage, it consists of the only starting piece.
    - Print the player's pieces, Your pieces:, and then one piece per line, enumerated.
    - Print the status of the game:
    - If status = "computer", print "Status: Computer is about to make a move. Press Enter to continue..."
    - If status = "player", print "Status: It's your turn to make a move. Enter your command."
    - Note that both these statuses suppose that the next move will be made, but at this stage, the program should stop here. We will implement other statuses (like "win", "lose", and "draw") in the stages to come.

## Stage 3/5: Taking Turns 

    Modify your Stage 2 code:

    - At the end of the game, print one of the following phrases:
    - Status: The game is over. You won!
    - Status: The game is over. The computer won!
    - Status: The game is over. It's a draw!

    - Print only the first and the last three pieces of the domino snake separated by three dots if it exceeds six dominoes in length.

    - Add a game loop that will repeat the following steps until the game ends:

    - Display the current playing field (stage 2).

    - If it's a user's turn, prompt the user for a move and apply it. If the input is invalid (a not-integer or it exceeds limitations), request a new input with the following message: Invalid input. Please try again..

    - If it's a computer's turn, prompt the user to press Enter, randomly generate a move, and apply it.

    - Switch turns.
