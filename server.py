#-*- coding: utf-8 -*-

from tornado import websocket, web, ioloop
import tornado
import json

import sys
import os.path

sys.path.append('module')
from Board import Board

clients = []
board = Board()

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('MemoryGame.html')

class SocketHandler(tornado.websocket.WebSocketHandler):
	def open(self):
		if self not in clients:
			clients.append(self)
	
	def on_close(self):
		if self in clients:
			clients.remove(self)

class PlayHandler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	def get(self, *args):
		num = int(self.get_argument('num'))

		result = board.update(num)

		for client in clients:
			client.write_message(json.dumps(result))

		self.finish()

if __name__ == '__main__':
	handlers = [
			(r'/', IndexHandler),
			(r'/ws', SocketHandler),
			(r'/play', PlayHandler),
			]

	settings = dict(
			static_path=os.path.join(os.path.dirname(__file__), 'static'),
			)

	app = tornado.web.Application(handlers, **settings)

	port = 8080
	app.listen(port)
	tornado.ioloop.IOLoop.instance().start()
