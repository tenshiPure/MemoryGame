var Server = function() {
	this.up = function() {
		url = 'ws://127.0.0.1:4521/ws';
		ws = new WebSocket(url);

		ws.onopen = function() {
			console.log('WebSocket open!');
		};

		ws.onclose = function() {
			console.log('WebSocket close!')
		};

		ws.onmessage = function(e) {
			var marks = JSON.parse(e.data)['marks'];
			var judgement = JSON.parse(e.data)['judgement'];
			for (var index in marks) {
				document.getElementById(index).src = "static/image/" + marks[index] + ".png";
			}

			if (judgement) {
				alert(judgement + ' player win!!!');
			}
		};
	};
}

new Server().up()
