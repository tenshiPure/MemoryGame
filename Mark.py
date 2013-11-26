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

	def __eq__(self, value):
		return self.value == value

	def output(self):
		print self.display,
