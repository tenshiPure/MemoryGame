#-*- coding: utf-8 -*-

from Board import Board

board = Board()

while True:
	x = input('x : ')
	y = input('y : ')

	board.update(x, y)
	board.output()
