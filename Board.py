#-*- coding: utf-8 -*-

from Turn import Turn
from Square import Square
from Mark import Mark

class Board:

	X = 3
	Y = 3

	def __init__(self):
		self.squares = [Square(Turn.SETUP, Mark.SPACE) for i in range(Board.X * Board.Y)]

	def update(self, x, y):
		self.squares[x + y * 3] = Square(Turn.getValue(), self.createMarkValue())
		Turn.next()

	def createMarkValue(self):
		return Mark.CROSS if Turn.isEven() else Mark.CERCLE

	def output(self):
		print ''
		for y in range(Board.Y):
			for x in range(Board.X):
				self.squares[x + y * 3].output()
			print ''
		print ''
