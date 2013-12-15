#-*- coding: utf-8 -*-

from Board import Board

board = Board()

print 'start game'

while not board.isFinish():
	num = input('num : ')

	print board.update(num)

print 'end game'
