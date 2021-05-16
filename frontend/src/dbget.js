const fetch = require("node-fetch");

fetch("http://127.0.0.1:8000/city/")
	.then(response => response.json())
	.then(myJson => console.log(myJson));
