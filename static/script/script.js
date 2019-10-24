function write() {
	// body...
	inputs = document.getElementsByTagName('input')
	for (var i = 0; i < inputs.length; i++) {
		inputs[i].value = inputs[i].name
	}
}

