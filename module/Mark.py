#-*- coding: utf-8 -*-

class Mark:

	BLANK  = 0
	CERCLE = 1
	CROSS  = 2

	def __init__(self, value, display):
		self.value = value
		self.display = display 

	@staticmethod
	def createMark(value):
		if value == Mark.BLANK:
			return Mark(value, '-')

		if value == Mark.CERCLE:
			return Mark(value, 'o')

		if value == Mark.CROSS:
			return Mark(value, 'x')

	def isBlank(self):
		return self.value == Mark.BLANK

	def createDisplay(self):
		return self.display

	def isSameAll(self, mark2, mark3):
		return self.value == mark2.value == mark3.value
