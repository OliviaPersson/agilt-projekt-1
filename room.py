class Room:
	def __init__(self, north, west, east, south, challenge_fn):
	#constructor
		self.north = north
		self.west = west
		self.east = east
		self.south = south
		self.challenge_fn = challenge_fn
#end class Room

def test1():
	print("Hello world")
	
def test2():
	print("Greetings, Earth")

r1 = Room(None, None, None, None, test1)
r2 = Room(None, None, None, r1, test2)
r1.north = r2
currentRoom = r1
command = ""

while(command != "quit"):
	command = input("What would you like to do? ")
	if(command == "north"):
		north = currentRoom.north
		if north:
			print("You go north.")
			currentRoom = north
		else:
			print("You cannot go that way.")
	elif(command == "west"):
		west = currentRoom.west
		if west:
			print("You go west.")
			currentRoom = west
		else:
			print("You cannot go that way.")
	elif(command == "east"):
		east = currentRoom.east
		if east:
			print("You go east.")
			currentRoom = east
		else:
			print("You cannot go that way.")
	elif(command == "south"):
		south = currentRoom.south
		if south:
			print("You go south.")
			currentRoom = south
		else:
			print("You cannot go that way.")
	elif(command == "challenge"):
		currentRoom.challenge_fn()
	else:
		print("Available commands: north west east south challenge quit")