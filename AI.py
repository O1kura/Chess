# declaration
scoreMap = {'K': 1000, 'Q': 90, 'R': 50, 'N': 30, 'B': 30, 'P': 10,
            'k': -1000, 'q': -90, 'r': -50, 'n': -30, 'b': -30, 'p': -10}
WinScore = 800
Depth = 3

# initialized in reverse order of row for easily observation
WhitePawnPos = [
    [10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0],
    [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
    [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
    [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
    [0.0,  0.0,  0.0,  1.5,  2.0,  0.0,  0.0,  0.0],
    [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  1.0],
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
    [-5.0, -1.5, -3.0, -3.0, -3.0, -3.0, -1.5, -5.0]]
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
    if board.is_checkmate():
        if board.turn == False:
            score = WinScore
        else:
            score = - WinScore
        return score
    elif board.is_stalemate():
        return 0
    else:
       score = 0
       for i in board.piece_map().values():
          score += scoreMap.get(i.symbol())
       return score
# sorting move from queen -> pawn
def sortMove(board):
    moveList = []
    for x in board.legal_moves:
        moveList.append(x)
    for i in range(len(moveList)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        square1 = board.piece_at(moveList[i].from_square)
        for j in range(i + 1, len(moveList)):
            square2 = board.piece_at(moveList[j].from_square)
            if square1.piece_type < square2.piece_type:
                min_idx = j
        # Swap the found minimum element with
        # the first element
        moveList[i], moveList[min_idx] = moveList[min_idx], moveList[i]
    return moveList

#####minman algorithm
def findMoveNegaMaxAlphaBeta(board, depth, alpha, beta, white):
    global nextMove, counter
    counter +=1 #dem so nuoc ma may tinh toan duoc
    if white: turnMultiplier = - 1
    else: turnMultiplier = 1

    if depth ==0:
        return turnMultiplier * scoreBoard(board)

    maxScore = -WinScore

    for move in sortMove(board):
        newBoard = board.copy()
        newBoard.push(move)

        score = -findMoveNegaMaxAlphaBeta(newBoard, depth-1, -beta, -alpha, not white)
        score += movePos(board,move)
        if score > maxScore:
            maxScore = score
            if depth == Depth:
                nextMove = move

        if maxScore > alpha:
            alpha = maxScore
        if alpha >= beta:
            break
    return maxScore

#find move and push
def findBestMove(board,white):
    global nextMove, counter
    nextMove = None
    counter = 0
    findMoveNegaMaxAlphaBeta(board,Depth, -WinScore, WinScore, white)

    if nextMove is not None:
        board.push(nextMove)
    else: board.push(sortMove(board)[0])
