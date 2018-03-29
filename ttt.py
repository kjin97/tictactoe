from Tkinter import Tk, Button

class ticTacToe:
	def __init__(self, multiplayer = False):
		self.over = False
		self._board = [[0,0,0], [0,0,0], [0,0,0]]
		self._winner = 0
		self._turn = 0
		self._toPlay = 1
		self._multiplayer = multiplayer

	def play(self, row, col):
		if self._board[row][col]:
			return True
		else:
			self.playOn(row, col)

	def playOn(self, row, col):
		self._board[row][col] = self._toPlay
		self._turn += 1
		self._toPlay = -self._toPlay
		self._check()

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
		self._winner = player
		if player > 0:
			print("Player 1 wins!")
		elif player < 0:
			print("Player 2 wins!")
		else:
			print("It's a draw!")

	def printBoard(self):
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

	def AIPlay(self, player):
		for i in range(3):
			if sum(self._board[i]) == 2 * player:
				j = self._board[i].index(0)
				return self.playOn(i, j)
		for j in range(3):
			if sum([row[j] for row in self._board]) == 2 * player:
				i = [row[j] for row in self._board].index(0)
				return self.playOn(i, j)

		for i in range(3):
			if sum(self._board[i]) == 2 * -player:
				j = self._board[i].index(0)
				return self.playOn(i, j)
		for j in range(3):
			if sum([row[j] for row in self._board]) == 2 * -player:
				i = [row[j] for row in self._board].index(0)
				return self.playOn(i, j)

		if self._board[1][1]:
			if self._board[0][0]:
				if self._board[2][0]:
					if self._board[0][2]:
						if self._board[2][2]:
							if self._board[1][0]:
								if self._board[0][1]:
									if self._board[1][2]:
										return self.playOn(2, 1)
									else:
										return self.playOn(1, 2)
								else:
									return self.playOn(0, 1)
							else:
								return self.playOn(1, 0)
						else:
							return self.playOn(2, 2)
					else:
						return self.playOn(0, 2)
				else:
					return self.playOn(2, 0)
			else:
				return self.playOn(0, 0)
		else:
			return self.playOn(1, 1)

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
		newButton = Button(self._window, command = F2)


	def _createButton(self, row, col):
		play = lambda: self._board.play(row, col) 
		newButton = Button(self._window, command = play)
		newButton.grid(row = x, col = y)

	def _update(self):
		



def readInput():
	try:
		return input()
	except EOFError:
		exit()

def main():
	while True:
		players = 0
		while players not in ['1', '2']:
			print('How many players?')
			players = readInput()
		players = int(players)
		if players == 1:
			singlePlayer()
		else:
			multiPlayer()
		print('Type anything to play again, or Ctrl-D to exit')
		readInput()


def singlePlayer():
	cols = ['a', 'b', 'c']
	rows = ['3', '2', '1']
	game = ticTacToe()

	while not game.over:
		print('Where would you like to play?')
		square = readInput()
		if len(square) == 2 and \
		square[0] in cols and \
		square[1] in rows:
			if game.play(rows.index(square[1]), cols.index(square[0])):
				print('Please play on an empty square.')
			else:
				game.AIPlay(-1)
		else:
			print('Please play on a valid square in the following format:\n' +
				'a3|b3|c3\na2|b2|c2\na1|b1|c1')
		game.printBoard()

def multiPlayer():
	print('Oops! Multiplayer functionality not supported yet.')


if __name__ == '__main__':
    main()

