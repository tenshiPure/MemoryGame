#-*- coding: utf-8 -*-

class Mark:

	SPACE  = 0
	CERCLE = 1
	CROSS  = 2

	def __init__(self, value, display):
		self.value = value
		self.display = display 

	@staticmethod
	def createMark(value):
		if value == Mark.SPACE:
			return Mark(value, '-')

		if value == Mark.CERCLE:
			return Mark(value, 'o')

		if value == Mark.CROSS:
			return Mark(value, 'x')

	def output(self):
		print self.display,
