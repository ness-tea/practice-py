def drawBoard(height, width):
    hstroke = "--- "
    vstroke = "|   "
    
    num_hstrokes = width
    num_vstrokes = width + 1
    num_printlines = 2*height + 1

    for i in range(num_printlines):
        if i % 2 == 1:
            row = ""
            for j in range(num_vstrokes):
                row += vstroke
            print(row)
            
        else:
            row = " "
            for j in range(num_hstrokes):
                row += hstroke
            print(row)
            

if __name__=="__main__":
    height = int(input("How tall do you want your gameboard?: "))
    width = int(input("How wide do you want your gameboard?: "))
    drawBoard(height, width)
