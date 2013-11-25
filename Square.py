#-*- coding: utf-8 -*-

from Mark import Mark

class Square:

	def __init__(self, turn, value):
		self.turn = turn
		self.mark = Mark.createMark(value)

	def output(self):
		self.mark.output()
