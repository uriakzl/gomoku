def search_max(board):
    #to find optimal move for black
    greatestScore = 0
    y = 0
    x = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                board[i][j] = "b"
                if is_win(board) == "Black won":
                    return (i,j)
                if greatestScore < score(board):
                    print(score(board))
                    greatestScore = score(board)
                    y = i
                    x = j

                board[i][j] = " "

    return (y, x)

def is_win(board):
    board_size = len(board)

    # Helper function to check for 5-in-a-row in any given direction
    def check_five_in_a_row(y, x, d_y, d_x, color):
        for i in range(5):
            new_y = y + i * d_y
            new_x = x + i * d_x
            if new_y < 0 or new_y >= board_size or new_x < 0 or new_x >= board_size or board[new_y][new_x] != color:
                return False
        return True

    # Check for winning sequences of 5 stones for both colors
    for y in range(board_size):
        for x in range(board_size):
            if board[y][x] == "b":
                if (check_five_in_a_row(y, x, 0, 1, "b") or  # Horizontal
                    check_five_in_a_row(y, x, 1, 0, "b") or  # Vertical
                    check_five_in_a_row(y, x, 1, 1, "b") or  # Diagonal (top-left to bottom-right)
                    check_five_in_a_row(y, x, 1, -1, "b")):  # Diagonal (top-right to bottom-left)
                    return "Black won"
            elif board[y][x] == "w":
                if (check_five_in_a_row(y, x, 0, 1, "w") or  # Horizontal
                    check_five_in_a_row(y, x, 1, 0, "w") or  # Vertical
                    check_five_in_a_row(y, x, 1, 1, "w") or  # Diagonal (top-left to bottom-right)
                    check_five_in_a_row(y, x, 1, -1, "w")):  # Diagonal (top-right to bottom-left)
                    return "White won"

    # Check for a draw if the board is full
    for row in board:
        if " " in row:
            return "Continue playing"

    return "Draw"


def detect_rows(board, col, length):
    '''
    use for loop to go through entire board to check each possible row
    then use detect row to check and count all the sequences
    return the sequences and done
    '''

    open_seq = 0
    semi_seq = 0

    #check the vertical columns first (d_y = 1, d_x = 0)
    for i in range(len(board)):
        temp = detect_row(board, col, 0, i, length, 1, 0)
        open_seq = open_seq + temp[0]
        semi_seq = semi_seq + temp[1]

    #then check the horizontal columns (d_y = 0, d_x = 1)
    for i in range(len(board)):
        temp = detect_row(board, col, i, 0, length, 0, 1)
        open_seq = open_seq + temp[0]
        semi_seq = semi_seq + temp[1]

    #check upper left to lower right (d_y = 1, d_x = 1)
    for i in range(len(board)):
        temp = detect_row(board, col, i, 0, length, 1, 1)
        open_seq = open_seq + temp[0]
        semi_seq = semi_seq + temp[1]

    for i in range(1, len(board)):
        temp = detect_row(board, col, 0, i, length, 1, 1)
        open_seq = open_seq + temp[0]
        semi_seq = semi_seq + temp[1]

    #check upper right lower left (d_y = 1, d_x = -1)
    for i in range(len(board)):
        temp = detect_row(board, col, 0, i, length, 1, -1)
        open_seq = open_seq + temp[0]
        semi_seq = semi_seq + temp[1]

    for i in range(1, len(board)):
        temp = detect_row(board, col, i, len(board)-1, length, 1, -1)
        open_seq = open_seq + temp[0]
        semi_seq = semi_seq + temp[1]

    #final return
    return (open_seq, semi_seq)

def detect_row(board, col, y_start, x_start,length, d_y, d_x):
    '''
    General Approach:
    put data into a straight list and then analyze the list based off the
    needed properties
    '''

    Row_List = []
    x_count = x_start
    y_count = y_start

    #for bottom to top
    if d_y == 1 and d_x == 0:
        while y_count < len(board):
            Row_List.append(board[y_count][x_count])
            y_count = y_count + 1

    #for left to right
    if d_y == 0 and d_x == 1:
        while x_count < len(board):
            Row_List.append(board[y_count][x_count])
            x_count = x_count + 1

    #from upper left to lower right
    if d_y == 1 and d_x == 1:
        while x_count < len(board) and y_count < len(board):
            Row_List.append(board[y_count][x_count])
            x_count = x_count + 1
            y_count = y_count + 1

    #from upper right to lower left
    if d_y == 1 and d_x == -1:
        while x_count >= 0 and y_count < len(board) :
            Row_List.append(board[y_count][x_count])
            x_count = x_count - 1
            y_count = y_count + 1

    open_count = 0
    semiopen_count = 0

    for i in range(len(Row_List) - length + 1):
        left_bound = False
        right_bound = False
        flag = False

        #check if the element is the right colour
        if Row_List[i] == col:
            #now if it is right colour, check if the next elements are correct
            for j in range(1, length):
                if Row_List[i+j] == col:
                    pass

                else:
                    flag = True


            if i + length > len(Row_List):
                if Row_List[i+length] == col:
                    flag = True


            if i != 0 and Row_List[i-1] == col:
                flag = True

            #it is the right colour and the next few elements all match, analyze
            #the sequence to see if it is open or semi open
            if not flag:
                #check left bound
                if i - 1 < 0:
                    left_bound = True

                else:
                    if Row_List[i-1] == " ":
                        pass
                    else:
                        left_bound = True


                #check right bound
                if i + length >= len(Row_List):
                    right_bound = True

                else:
                    if Row_List[i+length] == " ":
                        pass
                    else:
                        right_bound = True

                #final logic
                if left_bound == True and right_bound == True:
                    pass

                elif left_bound == False and right_bound == False:
                    open_count += 1

                else:
                    semiopen_count += 1

    return (open_count, semiopen_count)

def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def detect_rows(board, col, length):
    '''
    use for loop to go through entire board to check each possible row
    then use detect row to check and count all the sequences
    return the sequences and done
    '''

    open_seq = 0
    semi_seq = 0

    #check the vertical columns first (d_y = 1, d_x = 0)
    for i in range(len(board)):
        temp = detect_row(board, col, 0, i, length, 1, 0)
        open_seq = open_seq + temp[0]
        semi_seq = semi_seq + temp[1]

    #then check the horizontal columns (d_y = 0, d_x = 1)
    for i in range(len(board)):
        temp = detect_row(board, col, i, 0, length, 0, 1)
        open_seq = open_seq + temp[0]
        semi_seq = semi_seq + temp[1]

    #check upper left to lower right (d_y = 1, d_x = 1)
    for i in range(len(board)):
        temp = detect_row(board, col, i, 0, length, 1, 1)
        open_seq = open_seq + temp[0]
        semi_seq = semi_seq + temp[1]

    for i in range(1, len(board)):
        temp = detect_row(board, col, 0, i, length, 1, 1)
        open_seq = open_seq + temp[0]
        semi_seq = semi_seq + temp[1]

    #check upper right lower left (d_y = 1, d_x = -1)
    for i in range(len(board)):
        temp = detect_row(board, col, 0, i, length, 1, -1)
        open_seq = open_seq + temp[0]
        semi_seq = semi_seq + temp[1]

    for i in range(1, len(board)):
        temp = detect_row(board, col, i, len(board)-1, length, 1, -1)
        open_seq = open_seq + temp[0]
        semi_seq = semi_seq + temp[1]

    #final return
    return (open_seq, semi_seq)

if __name__ == "__main__":
    board = [["b"," "," "," "," "],
            ["b"," "," "," "," "],
            ["b"," "," "," "," "],
            [" "," "," "," "," "],
            [" "," "," "," "," "]]


    print(detect_rows(board, "b", 1))
    print(search_max(board))