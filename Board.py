#-*- coding: utf-8 -*-

from Turn import Turn
from Square import Square
from Mark import Mark

class Board:

	X = 3
	Y = 3

	def __init__(self):
		self.squares = [Square(Turn.SETUP, Mark.BLANK) for i in range(Board.X * Board.Y)]

	def update(self, x, y):
		if not self.isBlank(x, y):
			return

		self.squares[self.convert(x = x, y = y)] = Square(Turn.getValue(), self.createMarkValue())
		Turn.next()

	def createMarkValue(self):
		return Mark.CROSS if Turn.isEven() else Mark.CERCLE

	def convert(self, x = None, y = None, num = None):
		if num is None:
			return x + y * Board.X

		return (num % Board.X, num / Board.Y)

	def output(self, square, i):
		square.output()
		if i % Board.X == Board.X - 1:
			print ''

	def isBlank(self, x, y):
		return self.squares[self.convert(x = x, y = y)] == Mark.BLANK

	def play(self):
		print ''
		[self.output(square, index) for index, square in enumerate(self.squares)]
		print ''

		return True if not self.isFinish() else False

	def isFinish(self, nums = [0, 1, 2]):
		results = []
		results.append(self.check([0, 1, 2]))
		results.append(self.check([3, 4, 5]))
		results.append(self.check([6, 7, 8]))
		results.append(self.check([0, 3, 6]))
		results.append(self.check([1, 4, 7]))
		results.append(self.check([2, 5, 8]))
		results.append(self.check([0, 4, 8]))
		results.append(self.check([2, 4, 6]))

		return True in results

	def check(self, nums):
		square1 = self.squares[nums[0]].mark.value
		square2 = self.squares[nums[1]].mark.value
		square3 = self.squares[nums[2]].mark.value

		return (square1 == square2 == square3) and square1 != Mark.BLANK
