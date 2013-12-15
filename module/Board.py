#-*- coding: utf-8 -*-

from Turn import Turn
from Square import Square
from Mark import Mark

class Board:

	X = 3
	Y = 3

	def __init__(self):
		self.squares = [Square(Turn.SETUP, Mark.BLANK) for i in range(Board.X * Board.Y)]

	def update(self, num):
		if not self.isBlank(num):
			return self.createResult()

		self.squares[num] = Square(Turn.getValue(), self.createMarkValue())
		Turn.next()

		return self.createResult()

	def createMarkValue(self):
		return Mark.CROSS if Turn.isEven() else Mark.CERCLE

	def isBlank(self, num):
		return self.squares[num] == Mark.BLANK

	def createResult(self):
		result = {'marks' : [], 'judgement' : None}
		result['marks'] = [square.mark.display for square in self.squares]
		result['judgement'] = self.isFinish()

		return result

	def isFinish(self):
		petterns = [
				(0, 1, 2),
				(3, 4, 5),
				(6, 7, 8),
				(0, 3, 6),
				(1, 4, 7),
				(2, 5, 8),
				(0, 4, 8),
				(2, 4, 6)
				]

		for pettern in petterns:
			if self.check(pettern):
				return True

	def check(self, nums):
		square1 = self.squares[nums[0]].mark.value
		square2 = self.squares[nums[1]].mark.value
		square3 = self.squares[nums[2]].mark.value

		return (square1 == square2 == square3) and square1 != Mark.BLANK
