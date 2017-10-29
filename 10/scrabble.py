TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10), (7,7))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

def make_scrabble_board():
    board=[]
    for i in range(15):
        line=[]
        for i in range(15):
            line.append('_')
        board.append(line)

    for r,c in TRIPLE_WORD_SCORE:
        board[r][c] = 'T'

    for r,c in DOUBLE_WORD_SCORE:
        board[r][c] = 'D'

    for r,c in TRIPLE_LETTER_SCORE:
        board[r][c]='t'

    for r,c in DOUBLE_LETTER_SCORE:
        board[r][c] = 'd'
    return board
    
rawvals = {
    "aeioulnrst"  : 1,
    "dg"          : 2,
    "bcmp"        : 3,
    "fhvwy"       : 4,
    "k"           : 5,
    "jx"          : 8,
    "qz"          : 10 
}


scores = {}
for k in rawvals:
    for letter in k:
        scores[letter] = rawvals[k]



def add_word_across(board,word,r,c):
    y = c
    score = 0
    scoretemp = 0
    doubles = 0
    triples = 0
    for x in word:
        scoretemp = 0
        scoretemp = scores[x]
        if board[r][y] == "d":
            scoretemp = scoretemp * 2
        if board[r][y] == "t":
            scoretemp = scoretemp * 3
        if board[r][y] == "D":
            doubles = doubles + 1
        if board[r][y] == "T":
            triples = triples + 1
        board[r][y]= x
        score = score + scoretemp
        y = y + 1
    for i in range(0,doubles):
        score = score * 2
    for i in range(0,triples):
        score = score * 3
    return score
    
def add_word_down(board,word,r,c):
    y = r
    score = 0
    scoretemp = 0
    doubles = 0
    triples = 0
    for x in word:
        scoretemp = 0
        scoretemp = scores[x]
        if board[y][c] == "d":
            scoretemp = scoretemp * 2
        if board[y][c] == "t":
            scoretemp = scoretemp * 3
        if board[y][c] == "D":
            doubles = doubles + 1
        if board[y][c] == "T":
            triples = triples + 1
        board[y][c] = x
        score = score + scoretemp
        y = y + 1
    for i in range(0,doubles):
        score = score * 2
    for i in range(0,triples):
        score = score * 3
    return score
    
def print_board(b):
    for line in b:
        print ( ' '.join(line))
        

boarde = make_scrabble_board()
print(add_word_across(boarde,"hello",2,3))
print_board(boarde)
print(add_word_down(boarde,"goodbye",5,7))
print_board(boarde)