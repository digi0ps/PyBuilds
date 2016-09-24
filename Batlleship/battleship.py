from math import sqrt;
from random import randint;

#Board Class
class Board(object):
	board = []; #The main board;
	col = 0;
	row = 0;
	def __init__(self, l, s, t):
		#Sets the maximum points based on the difficulty given;
		if l=="d":
			p = 300;
		elif l=="m":
			p = 200;
		else: 
			p = 100;
		#Initialising variables
		self.level = l;
		self.size = s;
		self.turns = t;
		self.points = p;
		del p;
		self.createBoard();
		self.initBoard();
		self.board[self.row][self.col]="X";
		self.printBoard();

	def createBoard(self):
		for x in range(0,self.size):
			self.board.append(['O'] * self.size); 
	
	def printBoard(self):
		for i in range(0, self.size):
			print("  ".join(self.board[i]))
			
	def printDetails(self):
		print("level: " + str(self.level));
		print("size: " + str(self.size));
		print("turns: " + str(self.turns));
		print("points: " + str(self.points));

	def initBoard(self):
		self.row = randint(0, self.size-1);
		self.col = randint(0, self.size-1);		

#main
b = Board("d", 5, 10);

