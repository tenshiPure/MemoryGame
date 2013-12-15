#-*- coding: utf-8 -*-

from Turn import Turn
from Square import Square
from Mark import Mark

class Board:

	def __init__(self):
		self.squares = [Square(Turn.SETUP, Mark.BLANK) for i in range(9)]

	def update(self, num):
		if self.isBlank(num):
			self.squares[num] = Square(Turn.getValue(), self.createMarkValue())
			Turn.next()

		return self.createResult()

	def createMarkValue(self):
		return Mark.CROSS if Turn.isEven() else Mark.CERCLE

	def isBlank(self, num):
		return self.squares[num].isBlank()

	def createResult(self):
		result = {}
		result['marks'] = [square.createDisplay() for square in self.squares]

		if self.isFinish():
			result['judgement'] = Mark.CERCLE if Turn.isEven() else Mark.CROSS
		else:
			result['judgement'] = None

		return result

	def isFinish(self):
		petterns = [(0, 1, 2),(3, 4, 5),(6, 7, 8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6)]

		return True in [self.check(pettern) for pettern in petterns] 

	def check(self, nums):
		square1 = self.squares[nums[0]]
		square2 = self.squares[nums[1]]
		square3 = self.squares[nums[2]]

		return square1.isSameAll(square2, square3) and not square1.isBlank()
