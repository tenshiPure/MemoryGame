#-*- coding: utf-8 -*-

from Board import Board

board = Board()

print 'start game'

while board.play():
	x = input('x : ')
	y = input('y : ')

	board.update(x, y)

print 'end game'
