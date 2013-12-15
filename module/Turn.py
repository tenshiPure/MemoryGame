#-*- coding: utf-8 -*-

class Turn:

	DEFAULT = 0
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

	@staticmethod
	def isTooOld(square):
		return square.turn == Turn.getValue() - 6
