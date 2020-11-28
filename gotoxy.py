def gotoxy(x: int,y: int):
    'This function willl print text on the terminal based on the given position or coordinates'
    print ("­­­­­­­­­­­­­­%c[%d;%df" % (0x1B, y, x), end='')