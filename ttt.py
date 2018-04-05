from tkinter import Tk, Button, PhotoImage, Label #, Text
import sys

class ticTacToe:
	def __init__(self, multiplayer = False):
		self.over = False
		self.board = [[0,0,0], [0,0,0], [0,0,0]]
		self.winner = 0
		self._turn = 0 # increments every square played
		self.to_play = 1 # 1 for player 1, -1 for player 2
		# self._multiplayer = multiplayer # unused for now

	def play(self, row, col):
		# returns True if unplayable on square, else no return value.
		if self.board[row][col]:
			return True
		else:
			self._play_on(row, col)

	def _play_on(self, row, col):
		self.board[row][col] = self.to_play
		self._turn += 1
		self.to_play = -self.to_play
		self._check()

	def _undo_move(self, row, col):
		self.board[row][col] = 0
		self._turn -= 1
		self.to_play = -self.to_play

	def _check(self):
		for row in self.board:
			if sum(row) == 3:
				return self._win(1)
			if sum(row) == -3:
				return self._win(-1)
		for i in range(3):
			if sum([row[i] for row in self.board]) == 3:
				return self._win(1)
			if sum([row[i] for row in self.board]) == -3:
				return self._win(-1)
		if self.board[1][1] == 1:
			if self.board[0][2] + self.board[2][0] == 2:
				return self._win(1)
			if self.board[0][0] + self.board[2][2] == 2:
				return self._win(1)
		if self.board[1][1] == -1:
			if self.board[0][2] + self.board[2][0] == -2:
				return self._win(-1)
			if self.board[0][0] + self.board[2][2] == -2:
				return self._win(-1)
		if self._turn == 9:
			return self._win(0)

	def _win(self, player):
		self.over = True
		self.winner = player
		return player

	def print_board(self):
		for row in self.board:
			line = ' '
			for square in row:
				if square > 0:
					line += ('X ')
				elif square < 0:
					line += ('O ')
				else:
					line += ('_ ')
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
					if not self.board[i][j]:
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
					if not self.board[i][j]:
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
		# 	if sum(self.board[i]) == 2 * player:
		# 		j = self.board[i].index(0)
		# 		return self._play_on(i, j)
		# for j in range(3):
		# 	if sum([row[j] for row in self.board]) == 2 * player:
		# 		i = [row[j] for row in self.board].index(0)
		# 		return self._play_on(i, j)

		# for i in range(3):
		# 	if sum(self.board[i]) == 2 * -player:
		# 		j = self.board[i].index(0)
		# 		return self._play_on(i, j)
		# for j in range(3):
		# 	if sum([row[j] for row in self.board]) == 2 * -player:
		# 		i = [row[j] for row in self.board].index(0)
		# 		return self._play_on(i, j)

		# if self.board[1][1]:
		# 	for i in range(3):
		# 		for j in range(3):
		# 			if not self.board[i][j]:
		# 				if (sum([row[j] for row in self.board]) == player) and \
		# 				sum(self.board[i]) == player:
		# 					return self._play_on(i, j)
		# 				if (sum([row[j] for row in self.board]) == -player) and \
		# 				sum(self.board[i]) == -player:
		# 					return self._play_on(i, j)

		# if self.board[1][1]:

		# # 	for i in range(3):
		# # 		if sum(self.board[i]) == player:
		# # 			for j in range(3):
		# # 				if not self.board[i][j]:
		# # 					return self._play_on(i, j)
		# # 	for j in range(3):
		# # 		if sum([row[j] for row in self.board]) == player:
		# # 			for i in range(3):
		# # 				if not self.board[i][j]:
		# # 					return self._play_on(i, j)
		# # 	for i in range(3):
		# # 		if sum(self.board[i]) == -player:
		# # 			for j in range(3):
		# # 				if not self.board[i][j]:
		# # 					return self._play_on(i, j)
		# # 	for j in range(3):
		# # 		if sum([row[j] for row in self.board]) == -player:
		# # 			for i in range(3):
		# # 				if not self.board[i][j]:
		# # 					return self._play_on(i, j)
				
		# 	if self.board[0][0]:
		# 		if self.board[2][0]:
		# 			if self.board[0][2]:
		# 				if self.board[2][2]:
		# 					if self.board[1][0]:
		# 						if self.board[0][1]:
		# 							if self.board[1][2]:
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
		self._game = ticTacToe()
		self._AI = False
		self._grid = [[None,None,None] for i in range(3)]
		self._X = PhotoImage(file = 'x.gif')
		self._O = PhotoImage(file = 'o.gif')
		self._blank = PhotoImage(file = 'blank.gif')
		self._win_dialog = None
		for i in range(3):
			for j in range(3):
				self._grid[i][j] = self._createButton(i, j)
		sp_button = Button(self._window, command = self._single_player, width = 16, text = 'New 1 Player Game')
		sp_button.grid(row = 3, column = 1)
		mp_button = Button(self._window, command = self._multi_player, width = 16, text = 'New 2 Player Game')
		mp_button.grid(row = 4, column = 1)
		# self.win_msg = Text(self._window, font = ("Verdana", 32), width = 12, height = 1)
		# self.win_msg.tag_configure("center", justify='center')

		self._window.mainloop()


	def _createButton(self, row, col):
		
		def play():
			self._game.play(row, col)
			self._update()
			if self._AI and not self._game.over:
				self._game.AI_play()
				self._update()

		new_button = Button(self._window, command = play, width = 160, height = 160, image = self._blank)
		new_button.grid(row = row, column = col)
		new_button.image = self._blank
		return new_button

	def _update(self):
		for row in range(3):
			for col in range(3):
				if self._game.board[row][col]:
					self._grid[row][col].config(state = 'disabled')
					if self._game.board[row][col] > 0:
						self._grid[row][col].config(image = self._X)
						self._grid[row][col].image = self._X
					if self._game.board[row][col] < 0:
						self._grid[row][col].config(image = self._O)
						self._grid[row][col].image = self._O
				else:
					self._grid[row][col].config(state = 'normal')
					self._grid[row][col].config(image = self._blank)


		# self._game.print_board()
		if self._game.over:
			for i in range(3):
				for j in range(3):
					self._grid[i][j].config(state = 'disabled')
			if self._AI:
				if self._game.winner > 0:
					# self.win_msg.insert(1.0, 'You Win!') # JK it'll never happen
					win_msg = 'You Win!'
				elif self._game.winner < 0:
					# self.win_msg.insert(1.0, 'You Lose!')
					win_msg = 'You Lose!'
				else:
					# self.win_msg.insert(1.0, 'It\'s a Draw!')
					win_msg = 'It\'s a Draw!'
			else:
				if self._game.winner > 0:
					# self.win_msg.insert(1.0, 'Player 1 Wins!')
					win_msg = 'Player 1 Wins!'
				elif self._game.winner < 0:
					# self.win_msg.insert(1.0, 'Player 2 Wins!')
					win_msg = 'Player 2 Wins!'
				else:
					#self.win_msg.insert(1.0, 'It\'s a Draw!')
					win_msg = 'It\'s a Draw!'
			# self.win_msg.tag_add("center", "1.0", "end")
			# self.win_msg.place(relx = 0.5, rely = 0.5)

			self._win_dialog = Label(self._window, text = win_msg, font = ('Helvetica', 32), justify = 'center')
			self._win_dialog.place(relx = 0.5, rely = 0.5, anchor = 'c')


	def _single_player(self):
		self._AI = True
		self._game = ticTacToe()
		if self._win_dialog:
			self._win_dialog.destroy()
			self._win_dialog = None
		for i in range(3):
			for j in range(3):
				self._grid[i][j].config(state = 'normal')
				self._grid[i][j].config(state = 'normal')
		self._update()


	def _multi_player(self):
		self._AI = False
		self._game = ticTacToe()
		if self._win_dialog:
			self._win_dialog.destroy()
			self._win_dialog = None
		for i in range(3):
			for j in range(3):
				self._grid[i][j].config(state = 'normal')
				self._grid[i][j].config(state = 'normal')
		self._update()


def read_input():
	try:
		return input()
	except EOFError:
		exit()

def main():
	if len(sys.argv) > 1 and sys.argv[1] == '--gui':
		gui = GUI()
	else:
		players = 0
		while players not in ['1', '2']:
			print('How many players?')
			players = read_input()
		players = int(players)
		while True:
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

	answers = ['y', 'n']
	response = ''
	while response not in answers:
		print('Would you like to start? Type y for yes and n for no')
		response = read_input()[0]
	if response == 'n':
		game.play(1, 1)
		game.print_board()
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

