import random

pieceScore = {'K': 0, 'Q': 10, 'R': 5, 'N': 3, 'B': 2, 'p': 1}
CHECKMATE = 1000
STALEMATE = 0

# Function to score the board according to how much 
# material(pieces) is remaining on the board 
def scoreMaterial(board):
    score = 0
    for row in board:
        for square in row:
            if square[0] == 'w':
                score += pieceScore[square[1]]
            elif square[0] == 'b':
                score -= pieceScore[square[1]]
    return score

# AI to get the best move possible
def getBestMove(gs, validMoves):
    # white aims to drive the score closer to 1000 
    # black aims to drive the score closer to -1000
    turnMultiplier = 1 if gs.white_to_move else -1
    maxScore = -CHECKMATE
    bestMove = None
    for playerMove in validMoves:
        gs.makeMove(playerMove)

        # Evaluating the score of the board based on its state 
        # i.e. checkmate/stalemate
        if gs.checkmate:
            score = CHECKMATE
        elif gs.stalemate:
            score = STALEMATE
        else:
            score = turnMultiplier * scoreMaterial(gs.board)

        # Updating score and move if a better move is found
        # which improves the score for white/black 
        if score > maxScore:
            score = maxScore
            bestMove = playerMove
        
        gs.undoMove()

    return bestMove

def findRandomMove(validMoves):
    return random.choice(validMoves)