# declaration
scoreMap = {'K': 1000, 'Q': 110, 'R': 50, 'N': 30, 'B': 30, 'P': 10,
            'k': -1000, 'q': -110, 'r': -50, 'n': -30, 'b': -30, 'p': -10}
WinScore = 800
Depth = 4


# initialized in reverse order of row for easily observation
WhitePawnPos = [
    [10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0],
    [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
    [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
    [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
    [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
    [1.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  1.5],
    [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
    [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]]
WhiteKnightPos = [
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
    [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
    [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
    [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
    [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
    [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
    [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]]
WhiteBishopPos = [
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [-1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
    [-1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
    [-1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
    [-1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
    [-1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]]
WhiteRockPos = [
    [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]]
WhiteQueenPos = [
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [-1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [-1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]]
WhiteKingPos = [
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0],
    [2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]]


# reverse board (col 0 <-> 7, col 1 <-> 8, ... of the board)
# for changing from weighted positions from white to black
def reverseList(list2D):
    newList = []
    for row in list2D:
        newList = [row] + newList
    return newList


# get weighted positions of black side from white
BlackPawnPos = WhitePawnPos
BlackKnightPos = WhiteKnightPos
BlackBishopPos = WhiteBishopPos
BlackRockPos = WhiteRockPos
BlackQueenPos = WhiteQueenPos
BlackKingPos = WhiteKingPos

# reverse the lists for white (initialized in reverse order of row for easily observation)
WhitePawnPos = reverseList(BlackPawnPos)
WhiteKnightPos = reverseList(BlackKnightPos)
WhiteBishopPos = reverseList(BlackBishopPos)
WhiteRockPos = reverseList(BlackRockPos)
WhiteQueenPos = reverseList(BlackQueenPos)
WhiteKingPos = reverseList(BlackKingPos)

# combining all weighted positions above to one matrix 2D(12 matrices) -> 3D(2 matrices) -> 4D(1 matrix)
BlackPos = [BlackPawnPos, BlackKnightPos, BlackBishopPos, BlackRockPos, BlackQueenPos, BlackKingPos]
WhitePos = [WhitePawnPos, WhiteKnightPos, WhiteBishopPos, WhiteRockPos, WhiteQueenPos, WhiteKingPos]
PiecePos = [BlackPos, WhitePos]



# game check
def validMove(board):
    listMove = []
    for x in board.legal_moves:
        listMove.append(x.uci())
    return listMove

def endCheck(board):
    if(board.is_game_over()):
        outcome = board.outcome()
        if(outcome.winner):
            print("White win")
        else: print("black win")
        return False
    else: return True
# calculate change of position for the move
def movePos(board, move):
    intColor = int(board.piece_at(move.from_square).color)      #Black:False->0,white:True->1
    pieceType = board.piece_at(move.from_square).piece_type - 1 #Pown->King: 1-6 -> 0-5
    fromPos = move.from_square                                  #square:0->63 to convert to (row, col)
    fromRow = int(fromPos/8)
    fromCol = fromPos % 8
    toPos = move.to_square                                      #square:0->63 to convert to (row, col)
    toRow = int(toPos/8)
    toCol = toPos % 8
    # return = position to - position from
    return(PiecePos[intColor][pieceType][toRow][toCol] - PiecePos[intColor][pieceType][fromRow][fromCol])
#Score base on pieces values
def scoreBoard(board):
   score = 0
   for i in board.piece_map().values():
      score += scoreMap.get(i.symbol())

   return score
# find the best (max) move for player white
def maxValue(board, depth, beta):
    if board.is_checkmate():
        score = -WinScore if board.turn==False else WinScore
        return (score,None)
    if board.is_stalemate():
        return (0,None)
    if depth == 0:
        return (scoreBoard(board),None)                                   # depth limit

    valMax = -WinScore; alpha = -WinScore
    for move in board.legal_moves:
        newBoard = board.copy()
        newBoard.push(move)

        val = minValue(newBoard, depth-1, alpha)[0]
        if board.turn: val += movePos(board,move)                  # run with position calculation option

        if val >= beta: return (val, move)                      # alpha-beta prunning
        if alpha < val: alpha = val                             # alpha-beta prunning

        if valMax < val:
            (valMax, okmove) = (val, move)

    return (valMax, okmove)

# find the best (min) move for player black
def minValue(board, depth, alpha):
    if board.is_checkmate():
        score = -WinScore if board.turn==False else WinScore
        return (score,None)
    if board.is_stalemate():
        return (0,None)
    if depth == 0: return (scoreBoard(board),None)                                   # depth limit

    valMin = WinScore; beta = WinScore
    for move in board.legal_moves:
        newBoard = board.copy()
        newBoard.push(move)

        val = maxValue(newBoard, depth-1, beta)[0]
        if not board.turn : val -= movePos(board,move)                  # run with position calculation option

        if val <= alpha: return (val, move)                     # alpha-beta prunning
        if beta > val: beta = val                               # alpha-beta prunning

        if valMin > val:
            (valMin, okmove) = (val, move)

    return (valMin, okmove)

#Bot makes a move
def makeMove(board):
    if(board.turn):
        (score, move) = maxValue(board, Depth, WinScore)
    else: (score, move) = minValue(board, Depth, -WinScore)

    if move != None:
        board.push(move)