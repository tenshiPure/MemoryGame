var Server = function() {
	this.up = function() {
		url = 'ws://127.0.0.1:8080/ws';
		ws = new WebSocket(url);

		ws.onopen = function() {
			console.log('WebSocket open!');
		};

		ws.onclose = function() {
			console.log('WebSocket close!')
		};

		ws.onmessage = function(e) {
			console.log(e);
		};
	};
}

new Server().up()
