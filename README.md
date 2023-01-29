# BreakthroughGameAI
I want to create an extension to a previous breakthrough game project. I want to impliment more advanced AI that plans ahead multiple turns instead of just capturing when it can and moving randomly like in my old project. 
## Game description
Breakthrough is a two-player strategy board game. The game is played on a rectangular board divided into 8 x 8 squares, with each player starting on opposite sides of the board. The goal of the game is to advance one's own pieces across the board to the opponents side. Each player starts with 16 pieces, which can move one step up and diagonally left or right, they can only capture diagonally. The game is won by the player who reaches the other players side, or takes all the other players pieces, or gets into an immovable stalemate where the player with the most pieces left wins.
## Requirements 
- Programming language: Python
- Language language: English
- Opinto-ohjelma: Tietojenkäsittelytieteen kandiohjelma
- The game should have 2 modes of play, player vs AI, AI vs AI
- The AI should be able to find the best move according to it's multiple intrenal scenarios calculations and their results
- In the player vs AI mode of play the player has a way of controlling it's next move
- The gameboard will be visaulized through the python shell
- Each of the pieces moves is a function
- Each piece has a set of available moves, a piece is not able to be moved if it has no possible moves
- The position of the pieces is signified by the vertical and horizontal cordinates, say if a pieces is on x:2 and y:6, then it's position is 26
