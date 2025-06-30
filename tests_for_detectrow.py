#Tests for detect rows

x_start = 4
y_start = 0
length = 2
col = "b"

'''
board = [["w","w","w","b","b"],
        ["w"," ","w","w","b"],
        ["b"," ","w","w","b"],
        ["b"," ","b"," ","b"],
        ["b"," ","b"," ","b"]]

Row_List = []

x_count = x_start
y_count = y_start


#for upper right to lower left
while x_count >= 0 and y_count < len(board) :
    Row_List.append(board[y_count][x_count])
    x_count = x_count - 1
    y_count = y_count + 1

'''

open_count = 0
semiopen_count = 0
Row_List = [" ","b", "b", " ", " ", " ", " ", " "]
for i in range(len(Row_List) - length):
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
            if i + length > len(Row_List):
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



print(open_count)
print(semiopen_count)

