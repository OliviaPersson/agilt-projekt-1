import random

class TicTacToe:
	GAME_WIN = 0
	GAME_LOSS = 1
	GAME_TIE = 2
	
	def __init__(self):
	#Constructor
		self.board = [" "]*9
		self.free_spaces = list(range(9))
		self.players = ["X", "O"]
		self.game_result = -1 #placeholder value

	def display_board(self):
	#Shows visualization of the current board state
		print(self.board[0], "|", self.board[1], "|", self.board[2])
		print("-", "+", "-", "+", "-")
		print(self.board[3], "|", self.board[4], "|", self.board[5])
		print("-", "+", "-", "+", "-")
		print(self.board[6], "|", self.board[7], "|", self.board[8])

	def game_has_ended(self):
	#Determines whether the game has ended or if it's still going.
		for player in self.players:
			if self.is_winner(player):
				print(player + " is the winner!")
				self.game_result = TicTacToe.GAME_WIN if player == "X" else TicTacToe.GAME_LOSS
				return True			
		if not self.free_spaces: #No-one has won, but the board has no more free spaces.
			print("It's a draw!")
			self.game_result = TicTacToe.GAME_TIE
			return True
		return False #No-one has won, and it's not a draw, so the game hasn't ended yet.

	def is_winner(self, player):
	#Checks whether a player has won
		WIN_CONDITIONS = [
			[0,1,2], #top row
			[3,4,5], #middle row
			[6,7,8], #bottom row
			[0,3,6], #left column
			[1,4,7], #middle column
			[2,5,8], #right column
			[0,4,8], #top-left-to-bottom-right diagonal
			[2,4,6]  #bottom-left-to-top-right diagonal
			]
		#Check if any of the win conditions has been fully filled by a single player.
		for cond in WIN_CONDITIONS:
			if self.board[cond[0]] == self.board[cond[1]] == self.board[cond[2]] == player:
				return True
		return False

	def player_move(self, player):
	#Allows a player to make moves, and makes sure the move is valid.
		valid_move = False
		while not valid_move:
			try:
				location = int(input(player + ", choose a square (1-9): ")) - 1
				if location in self.free_spaces:
					self.board[location] = player
					self.free_spaces.remove(location)
					valid_move = True
				else:
					print("That is not a free space on the board.")
			except:
				print("Invalid input.")
	
	def play_multiplayer(self):
	#Starts a multiplayer game.
		currentPlayerID = 0
		while not self.game_has_ended():
			self.display_board()
			player = self.players[currentPlayerID]
			self.player_move(player)
			#pass control to the next player
			currentPlayerID = (currentPlayerID + 1) % len(self.players)
		self.display_board()
		return self.game_result
	
	def play_vs_AI(self):
	#Starts a game against a computer-controlled opponent.
		while not self.game_has_ended():
			self.display_board()
			self.player_move("X")
			if self.game_has_ended():
				break
			AI_move = self.free_spaces[random.randint(0,len(self.free_spaces)-1)]
			self.board[AI_move] = "O"
			self.free_spaces.remove(AI_move)
			print(f"AI chose square {AI_move + 1}.")
		self.display_board()
		return self.game_result
#end class TicTacToe