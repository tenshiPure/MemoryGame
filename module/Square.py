#-*- coding: utf-8 -*-

from Mark import Mark

class Square:

	def __init__(self, turn, value):
		self.turn = turn
		self.mark = Mark.createMark(value)

	def isBlank(self):
		return self.mark.isBlank()

	def createDisplay(self):
		return self.mark.createDisplay()

	def isSameAll(self, square2, square3):
		return self.mark.isSameAll(square2.mark, square3.mark)
