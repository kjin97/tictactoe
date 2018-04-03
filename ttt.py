from tkinter import Tk, Button

class ticTacToe:
	def __init__(self, multiplayer = False):
		self.over = False
		self._board = [[0,0,0], [0,0,0], [0,0,0]]
		self.winner = 0
		self._turn = 0 # increments every square played
		self.to_play = 1 # 1 for player 1, -1 for player 2
		# self._multiplayer = multiplayer # unused for now

	def play(self, row, col):
		# returns True if unplayable on square, else no return value.
		if self._board[row][col]:
			return True
		else:
			self._play_on(row, col)

	def _play_on(self, row, col):
		self._board[row][col] = self.to_play
		self._turn += 1
		self.to_play = -self.to_play
		self._check()

	def _undo_move(self, row, col):
		self._board[row][col] = 0
		self._turn -= 1
		self.to_play = -self.to_play

	def _check(self):
		for row in self._board:
			if sum(row) == 3:
				return self._win(1)
			if sum(row) == -3:
				return self._win(-1)
		for i in range(3):
			if sum([row[i] for row in self._board]) == 3:
				return self._win(1)
			if sum([row[i] for row in self._board]) == -3:
				return self._win(-1)
		if self._board[1][1] == 1:
			if self._board[0][2] + self._board[2][0] == 2:
				return self._win(1)
			if self._board[0][0] + self._board[2][2] == 2:
				return self._win(1)
		if self._board[1][1] == -1:
			if self._board[0][2] + self._board[2][0] == -2:
				return self._win(-1)
			if self._board[0][0] + self._board[2][2] == -2:
				return self._win(-1)
		if self._turn == 9:
			return self._win(0)

	def _win(self, player):
		self.over = True
		self.winner = player
		return player

	def print_board(self):
		for row in self._board:
			line = ' '
			for square in row:
				if square > 0:
					line += ('X ')
				elif square < 0:
					line += ('O ')
				else:
					line += ('  ')
			print(line)

	# Returns a tuple of optimal move and minimax value
	def minimax(self):
		winner = self._check()
		if winner:
			self.over = False
			self.winner = 0
			return (None, winner)
		if self._turn == 9:
			self.over = False
			self.winner = 0
			return (None, 0)
		if self.to_play == 1:
			best_val = -1
			best_move = None
			for i in range(3):
				for j in range(3):
					if not self._board[i][j]:
						self._play_on(i, j)
						move_val = self.minimax()[1]
						if move_val >= best_val:
							best_val = move_val
							best_move = (i, j)
						self._undo_move(i, j)
			return (best_move, best_val)
		else:
			best_val = 1
			best_move = None
			for i in range(3):
				for j in range(3):
					if not self._board[i][j]:
						self._play_on(i, j)
						move_val = self.minimax()[1]
						if move_val <= best_val:
							best_val = move_val
							best_move = (i, j)
						self._undo_move(i, j)
			return (best_move, best_val)


	def AI_play(self):
		i, j = self.minimax()[0]
		self._play_on(i, j)
		# for i in range(3):
		# 	if sum(self._board[i]) == 2 * player:
		# 		j = self._board[i].index(0)
		# 		return self._play_on(i, j)
		# for j in range(3):
		# 	if sum([row[j] for row in self._board]) == 2 * player:
		# 		i = [row[j] for row in self._board].index(0)
		# 		return self._play_on(i, j)

		# for i in range(3):
		# 	if sum(self._board[i]) == 2 * -player:
		# 		j = self._board[i].index(0)
		# 		return self._play_on(i, j)
		# for j in range(3):
		# 	if sum([row[j] for row in self._board]) == 2 * -player:
		# 		i = [row[j] for row in self._board].index(0)
		# 		return self._play_on(i, j)

		# if self._board[1][1]:
		# 	for i in range(3):
		# 		for j in range(3):
		# 			if not self._board[i][j]:
		# 				if (sum([row[j] for row in self._board]) == player) and \
		# 				sum(self._board[i]) == player:
		# 					return self._play_on(i, j)
		# 				if (sum([row[j] for row in self._board]) == -player) and \
		# 				sum(self._board[i]) == -player:
		# 					return self._play_on(i, j)

		# if self._board[1][1]:

		# # 	for i in range(3):
		# # 		if sum(self._board[i]) == player:
		# # 			for j in range(3):
		# # 				if not self._board[i][j]:
		# # 					return self._play_on(i, j)
		# # 	for j in range(3):
		# # 		if sum([row[j] for row in self._board]) == player:
		# # 			for i in range(3):
		# # 				if not self._board[i][j]:
		# # 					return self._play_on(i, j)
		# # 	for i in range(3):
		# # 		if sum(self._board[i]) == -player:
		# # 			for j in range(3):
		# # 				if not self._board[i][j]:
		# # 					return self._play_on(i, j)
		# # 	for j in range(3):
		# # 		if sum([row[j] for row in self._board]) == -player:
		# # 			for i in range(3):
		# # 				if not self._board[i][j]:
		# # 					return self._play_on(i, j)
				
		# 	if self._board[0][0]:
		# 		if self._board[2][0]:
		# 			if self._board[0][2]:
		# 				if self._board[2][2]:
		# 					if self._board[1][0]:
		# 						if self._board[0][1]:
		# 							if self._board[1][2]:
		# 								return self._play_on(2, 1)
		# 							else:
		# 								return self._play_on(1, 2)
		# 						else:
		# 							return self._play_on(0, 1)
		# 					else:
		# 						return self._play_on(1, 0)
		# 				else:
		# 					return self._play_on(2, 2)
		# 			else:
		# 				return self._play_on(0, 2)
		# 		else:
		# 			return self._play_on(2, 0)
		# 	else:
		# 		return self._play_on(0, 0)
		# else:
		# 	return self._play_on(1, 1)

class GUI:
	def __init__(self):
		self._window = Tk()
		self._window.title('Tic Tac Toe')
		self._board = ticTacToe()
		self._grid = [[None,None,None] for i in range(3)]
		for i in range(3):
			for j in range(3):
				self._grid[i][j] = self._createButton(i, j)
		F2 = lambda: self._newGame
		new_button = Button(self._window, command = F2)


	def _createButton(self, row, col):
		play = lambda: self._board.play(row, col) 
		new_button = Button(self._window, command = play)
		new_button.grid(row = x, col = y)

	def _update(self):
		pass
		



def read_input():
	try:
		return input()
	except EOFError:
		exit()

def main():
	while True:
		players = 0
		while players not in ['1', '2']:
			print('How many players?')
			players = read_input()
		players = int(players)
		if players == 1:
			winner = single_player()
		else:
			winner = multi_player()
		if winner > 0:
			print("Player 1 wins!")
		elif winner < 0:
			print("Player 2 wins!")
		else:
			print("It's a draw!")
		print('Type anything to play again, or Ctrl-D to exit')
		read_input()


def single_player():
	cols = ['a', 'b', 'c']
	rows = ['3', '2', '1']
	game = ticTacToe()

	while not game.over:
		print('Where would you like to play?')
		square = read_input()
		if len(square) == 2 and \
		square[0] in cols and \
		square[1] in rows:
			if game.play(rows.index(square[1]), cols.index(square[0])):
				print('Please play on an empty square.')
			else:
				if not game.over:
					game.AI_play()
		else:
			print('Please play on a valid square in the following format:\n' +
				'a3|b3|c3\na2|b2|c2\na1|b1|c1')
		game.print_board()
	return game.winner

def multi_player():
	cols = ['a', 'b', 'c']
	rows = ['3', '2', '1']
	game = ticTacToe()


	while not game.over:
		if game.to_play > 0:
			print('Player 1\'s turn to play')
		else:
			print('Player 2\'s turn to play')
		square = read_input()
		if len(square) == 2 and \
		square[0] in cols and \
		square[1] in rows:
			if game.play(rows.index(square[1]), cols.index(square[0])):
				print('Please play on an empty square.')
		else:
			print('Please play on a valid square in the following format:\n' +
				'a3|b3|c3\na2|b2|c2\na1|b1|c1')
		game.print_board()
	return game.winner


if __name__ == '__main__':
    main()

