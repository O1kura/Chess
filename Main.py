import tkinter
from tkinter import *
import chess
from PIL import ImageTk,Image

import AI
import AIc
#game declare
board = chess.Board()
white = True
def setWhite(choice):
    global white
    white = choice
#GUI declare
gui = tkinter.Tk()
gui.title("Chess")
#GUI variables
ROW_NUMBER = 8
COLUMN_NUMBER = 8
COL_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
WHITE = '#F0D9B5'
BLACK = '#B58863'
GREEN = '#646C00'
imgMap = {'K':'WK', 'Q':'WQ', 'R':'WR', 'N':'WN', 'B':'WB', 'P':'WP',
            'k':'Bk','q':'Bq','r':'Br','n':'Bn','b':'Bb','p':'Bp'}

square_size = 64
#for drawing pieces
pieces = {}
icons = {}
#later use
start_square = None
highlighted_pieces = []
undo_count= 0
def count_undo(choice):
    global undo_count
    if(choice):
        undo_count = undo_count + 1
    else:
        undo_count = undo_count - 1
        undo_count = max(0,undo_count)
    if undo_count > 2:
        undo_count = 2
        return False

    return True
#canvas and status bar declaration
canvas_width = COLUMN_NUMBER * square_size
canvas_height = ROW_NUMBER * square_size
canvas = tkinter.Canvas(gui,width=canvas_width, height=canvas_height, background='grey')
#statusbar = tkinter.Frame(gui, height=32)
label_status = tkinter.Label(text='', fg='black')
label_status.pack(side=tkinter.TOP, expand=0)
#statusbar.pack(expand=False, fill='x', side='bottom')
menu = tkinter.Menu(gui)
gui.config(menu = menu)
#a var for considering player move
playerTurn = True
def setPlayerTurn(cor):
    global playerTurn
    playerTurn = cor

#handle left click event
def click(event):
    # block clicks if not in player's turn
    if not playerTurn:
        return None

    column_size = row_size = square_size
    row = int(8 - (event.y / row_size))
    column = int(event.x / column_size)
    position = (row, column)

    # check if player is selecting their other piece
    piece = board.piece_at(row * 8 + column)
    if piece is not None and piece.symbol().islower() is not white:
    # move it or replace it
        global start_square
        start_square= position
        highlight(position)

    elif start_square is not None:
        move(dest_square=position)
        start_square = None

    refresh()
    highlighted_pieces.clear()
#draw the board( aka refresh for multiple uses)
def refresh():

    canvas.delete('square')
    color = BLACK

    for row in range(ROW_NUMBER):
        color = WHITE if color == BLACK else BLACK

        for col in range(COLUMN_NUMBER):
            start_column = (col * square_size)
            start_row = ((7 - row) * square_size)
            end_column = start_column + square_size
            end_row = start_row + square_size

            canvas.create_rectangle(
                start_column,
                start_row,
                end_column,
                end_row,
                outline='',
                fill=color,
                tags='square')

            if (row, col) in highlighted_pieces:
                canvas.create_oval(
                    start_column+square_size/4,
                    start_row+square_size/4,
                    end_column-square_size/4,
                    end_row-square_size/4,
                    outline='',
                    fill=GREEN,
                    tags='square')

            color = WHITE if color == BLACK else BLACK


    draw_pieces()

    canvas.tag_raise('piece')
    canvas.tag_lower('square')
#draw the pieces
def draw_pieces():
    canvas.delete('piece')

    for square in chess.SQUARES:
        piece = board.piece_at(square)

        if piece is not None:
            image_name = 'img/%s.png' % (imgMap.get(piece.symbol()))
            piece_name = '%s%s' % (piece.symbol(), square)

            if image_name not in icons:
                image = Image.open(image_name).resize((64, 64))
                icons[image_name] = ImageTk.PhotoImage(image)

            row = square // 8
            column = square % 8

            add_piece(piece_name, icons[image_name], row, column)

#place a piece to board
def add_piece(name, image, row=0, column=0):
    canvas.create_image(
        0, 0, image=image, tags=(name, 'piece'), anchor='c')
    place_piece(name, row, column)

def place_piece( name, row, column):
    pieces[name] = (row, column)
    row_size = (column * square_size) + (square_size // 2)
    column_size = ((7 - row) * square_size) + (square_size // 2)

    canvas.coords(name, row_size, column_size)
#player make a move
def move(dest_square):
    # making move notation
    move = COL_CHARS[start_square[1]] + str(start_square[0] + 1)
    move += COL_CHARS[dest_square[1]] + str(dest_square[0] + 1)

    # handle pawn promotion
    if move + 'q' in AI.validMove(board):
        move += 'q'

    if move in AI.validMove(board):
        board.push(chess.Move.from_uci(move))
        setPlayerTurn(False)
        count_undo(False)
        label_status[ 'text'] = "Computer's turn. The computer is thinking..."
        refresh()
        gui.after(1000, botMove)
    else:
        label_status['text'] = "Wrong move, try again."
    endcheck()
    refresh()
#highlight possible moves
def highlight(position):

    legal_moves = AI.validMove(board)
    selected_square = COL_CHARS[position[1]] + str(position[0] + 1)
    for legal_move in legal_moves:
        if selected_square == legal_move[:2]:
            #promotion
            if(legal_move[-1] in 'qnbr'):
                highlighted_pieces.append((int(legal_move[-2]) - 1,COL_CHARS.index(legal_move[2])))
            else:
                highlighted_pieces.append((int(legal_move[-1]) - 1,COL_CHARS.index(legal_move[2])))

#botmove
def botMove():
    AI.makeMove(board)
    #AIc.findMoveNegaMax(board,board.legal_moves,2,1)
    setPlayerTurn(True)
    label_status["text"] = "Your turn"
    endcheck()
    refresh()
#undo
def undo():
    if not playerTurn:
        return None
    #else:
    elif count_undo(True) and len(board.move_stack) != 0:
        board.pop()
        board.pop()
        refresh()
    else:
        return None
btn = tkinter.Button(text = 'Undo',command = undo)
btn.pack(side = tkinter.BOTTOM)
#bind mouse left click
canvas.bind("<Button-1>", click)
#refresh
canvas.pack()
refresh()
#start chess
def start():
    if white:
        label_status["text"] = "You play as white."

    else:
        label_status["text"] = "You play as black. The computer is thinking..."
        gui.after(1000,botMove())
    gui.mainloop()
#check game ending
def endcheck():
    if board.is_checkmate():
        label_status["text"] = "Checkmate."
        if board.turn:
            label_status["text"] = "Black win"
        else:
            label_status["text"] = "White win"
    elif board.is_stalemate():
        label_status["text"] = "It was a draw."
#restart option
def restart_white():
    setWhite(True)
    board.reset()
    refresh()
    start()
def restart_black():
    setWhite(False)
    board.reset()
    refresh()
    start()
#add restart to menu
sub1 = tkinter.Menu(menu)
sub2 = tkinter.Menu(sub1)
sub2.add_radiobutton(label = 'white',command = restart_white)
sub2.add_radiobutton(label = 'black',command = restart_black)
sub1.add_cascade(label = "Restart",menu = sub2)
sub1.add_separator()
menu.add_cascade(label = "Game",menu=sub1)
#run
start()

