#test for detectrows
#Question 3

def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board


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
                #if Row_List[i+length] == col:
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
        print(i, detect_row(board, col, i, 0, length, 0, 1))
        temp = detect_row(board, col, i, 0, length, 0, 1)
        open_seq = open_seq + temp[0]
        semi_seq = semi_seq + temp[1]

    #check upper left to lower right (d_y = 1, d_x = 1)
    for i in range(len(board)):
        temp = detect_row(board, col, i, 0, length, 1, 1)
        open_seq = open_seq + temp[0]
        semi_seq = semi_seq + temp[1]

    for i in range(0, len(board)-1):
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

if __name__ == "__main__":
    board = make_empty_board(8)
    put_seq_on_board(board, 1, 1, 0, 1, 2, "b")
    put_seq_on_board(board, 3, 1, 0, 1, 3, "b")
    put_seq_on_board(board, 5, 1, 0, 1, 4, "b")
    put_seq_on_board(board, 1, 4, 0, 1, 3, "w")
    put_seq_on_board(board, 2, 4, 0, 1, 3, "w")
    put_seq_on_board(board, 3, 5, 0, 1, 2, "w")
    put_seq_on_board(board, 4, 6, 0, 1, 1, "w")


    print(detect_rows(board, "b", 2))
