#random tester for gomoku

#Question 2
# assumes square board
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    #boolean values for simplicity (sort of)
    start_bounded = False
    end_bounded = False

    if d_y == 0 and d_x == 1: #left to right
        if length >= len(board):
            return "CLOSED"

        #check start bound
        if x_end - length + 1 < 1:
            start_bounded = True

        else:
            if board[y_end][x_end - length] == " ":
                pass
            else:
                start_bounded = True

        #check end bound
        if x_end + 1 >= (len(board)):
            end_bounded = True

        else:
            if board[y_end][x_end + 1] == " ":
                pass
            else:
                end_bounded = True

    elif d_y == 1 and d_x == 0: #top to bottom
        if length >= len(board):
            return "CLOSED"

        #check start bound
        if y_end - length + 1 < 1:
            start_bounded = True

        else:
            if board[y_end-length][x_end] == " ":
                pass
            else:
                start_bounded = True

        #check end bound
        if y_end + 1 >= len(board):
            end_bounded = True

        else:
            if board[y_end + 1][x_end] == " ":
                pass
            else:
                end_bounded = True

    elif d_y == 1 and d_x == 1: #upper left to lower right
        if length >= len(board):
            return "CLOSED"

        #check start bound
        if y_end - length + 1 < 1 or x_end - length + 1 < 1:
            start_bounded = True

        else:
            if board[y_end-length-1][x_end - length-1] == " ":
                pass
            else:
                start_bounded = True

        #check end bound
        if y_end + 1 >= (len(board)) or x_end + 1 >= (len(board)):
            end_bounded = True

        else:
            if board[y_end+1][x_end+1] == " ":
                pass
            else:
                end_bounded = True

    elif d_y == 1 and d_x == -1: #upper right to lower left
        if length >= len(board):
            return "CLOSED"

        #check start bound
        if y_end - length + 1 < 1 or  x_end + length + 1 > len(board):
            start_bounded = True

        else:
            if board[y_end-length-1][x_end + length] == " ":
                pass
            else:
                start_bounded = True

        #check end bound
        if y_end + 1 >= (len(board)) or x_end - 1 >= (len(board)):
            end_bounded = True

        else:
            if board[y_end +1][x_end -1] == " ":
                pass
            else:
                end_bounded = True


    #final logic
    if start_bounded == True and end_bounded == True:
        return "CLOSED"

    if start_bounded == False and end_bounded == False:
        return "OPEN"

    else:
        return "SEMIOPEN"

if __name__ == "__main__":
    board = [[" "," "," "," "],
             [" "," "," "," "],
             [" "," "," "," "],
             [" "," "," "," "]]
    #board, y_end, x_end, length, d_y, d_x
    print(is_bounded(board, 2, 1, 2, 1,-1))



