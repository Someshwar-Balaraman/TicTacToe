import random

dim = 3

#player 0's symbol is o
#player 1's symbol is x

def create_board(dim):
	board = [['_' for i in range(dim)] for j in range(dim)]
	return board

def print_board(board):
	for i in range(dim):
		print(board[i])
	print("\n")
	return

def is_board_full(board):
	for i in range(dim):
		for j in range(dim):
			if board[i][j] == '_':
				return False
	return True

def check_win(board):
	#check rows
	for i in range(dim):
		checker = board[i]
		if len(set(checker))==1 and checker[0]!='_':
			return True

	checker = [0 for i in range(dim)]
	#check columns
	for i in range(dim):
		k=0
		for j in range(dim):
			checker[k] = board[j][i]
			k+=1
		if len(set(checker))==1 and checker[0]!='_':
			return True

	#check diagonal 1
	i,j,k = 0,0,0
	for p in range(dim):
		checker[k] = board[i][j]
		k+=1
		i+=1
		j+=1
	#print(checker)
	if len(set(checker))==1 and checker[0]!='_':
			return True

	# check diagonal 2
	i=0
	j=2
	k=0
	for p in range(dim):
		checker[k] = board[i][j]
		k+=1
		i+=1
		j-=1
	if len(set(checker))==1 and checker[0]!='_':
			return True

	return False

def toggle(key):
	if key==0:
		return 1
	return 0

if __name__ == "__main__":

	board = create_board(dim)
	key= round(random.random())
	# print(key)

	while(1):
		print_board(board)
		#row, col = input("Player {} turn : (Enter row and column)".format(key)).split()
		print("Player {} turn : (Enter row and column)".format(key))
		row = input("row:")
		col = input("col:")
		row = int(row)
		col = int(col)
		row-=1
		col-=1
		print(row, col)
		if key==0:
			board[row][col] = 'o'
		else:
			board[row][col] = 'x'

		if check_win(board):
			print("Player {} won!!!".format(key))
			break
		print_board(board)

		if is_board_full(board):
			break
		key = toggle(key)



	#board = create_board(dim)
	#print_board(board)
	# testing
	# board = [['*','_','_'],['*', '*', '_'], ['*','_','_']]
	# print_board(board)
	# if check_win(board):
	# 	print("Won")
	# else:
	# 	print("Not yet")


