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
		self.squares[self.convert(x = x, y = y)] = Square(Turn.getValue(), self.createMarkValue())
		Turn.next()

	def createMarkValue(self):
		return Mark.CROSS if Turn.isEven() else Mark.CERCLE

	def convert(self, x = None, y = None, num = None):
		if num is None:
			return x + y * Board.X

		return (num % Board.X, num / Board.Y)

	def _output(self, square, i):
		square.output()
		if i % Board.X == Board.X - 1:
			print ''

	def output(self):
		print ''
		[self._output(square, index) for index, square in enumerate(self.squares)]
		print ''
