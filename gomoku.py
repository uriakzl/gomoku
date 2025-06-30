#Gomoku.py
#Question 1
def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != " ":
                return False

    return True


#Question 2
# assumes square board
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    print_board(board)

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
            if board[y_end-length][x_end - length] == " ":
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
        if y_end - length + 1 < 1 or x_end + length + 1 > len(board):
            start_bounded = True

        else:
            if board[y_end-length][x_end + length] == " ":
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

    elif start_bounded == False and end_bounded == False:
        return "OPEN"

    else:
        return "SEMIOPEN"

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
                flag = True

            if i != 0 and Row_List[i-1] == col:
                flag = True

            if i+length < len(Row_List) and Row_List[i+length] == col:
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

    for i in range(0, len(board)):
        temp = detect_row(board, col, 0, i+1, length, 1, 1)
        open_seq = open_seq + temp[0]
        semi_seq = semi_seq + temp[1]

    #check upper right lower left (d_y = 1, d_x = -1)
    for i in range(len(board)):
        temp = detect_row(board, col, 0, i, length, 1, -1)
        open_seq = open_seq + temp[0]
        semi_seq = semi_seq + temp[1]

    for i in range(0, len(board)):
        temp = detect_row(board, col, i+1, len(board)-1, length, 1, -1)
        open_seq = open_seq + temp[0]
        semi_seq = semi_seq + temp[1]

    #final return
    return (open_seq, semi_seq)

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
                if (check_five_in_a_row(y, x, 0, 1, "b") or
                    check_five_in_a_row(y, x, 1, 0, "b") or
                    check_five_in_a_row(y, x, 1, 1, "b") or
                    check_five_in_a_row(y, x, 1, -1, "b")):

                    return "Black won"

            elif board[y][x] == "w":
                if (check_five_in_a_row(y, x, 0, 1, "w") or
                    check_five_in_a_row(y, x, 1, 0, "w") or
                    check_five_in_a_row(y, x, 1, 1, "w") or
                    check_five_in_a_row(y, x, 1, -1, "w")):
                    return "White won"

    # Check for a draw if the board is full
    for row in board:
        if " " in row:
            return "Continue playing"

    return "Draw"



def detect_row_bad(board, col, y_start, x_start, length, d_y, d_x):
    if (y_start, x_start, d_x,d_y, length) == (5, 1, 0, 1, 3):
        return (1, 0)
    else:
        return (0, 0)


def search_max_bad(board):
    import random
    move_y = int(8*random.random())
    move_x = int(8*random.random())
    while move_y >= 0:
        move_y = int(8*random.random())
        move_x = int(8*random.random())



    return move_y, move_x



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

def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res





        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x

def tests(board):
    game_res = is_win(board)
    if game_res in ["White won", "Black won", "Draw"]:
        return game_res

def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()


def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0




if __name__ == '__main__':
    play_gomoku(8)
