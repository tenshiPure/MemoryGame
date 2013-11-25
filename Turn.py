#-*- coding: utf-8 -*-

class Turn:

	SETUP = 0
	VALUE = 1

	@staticmethod
	def initialize():
		Turn.VALUE = 1

	@staticmethod
	def getValue():
		return Turn.VALUE

	@staticmethod
	def next():
		Turn.VALUE += 1

	@staticmethod
	def isEven():
		return Turn.VALUE % 2 == 0
