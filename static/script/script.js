function write() {
	// body...
	inputs = document.getElementsByTagName('input')
	for (var i = 0; i < inputs.length; i++) {
		inputs[i].value = inputs[i].name
	}
}

/*

function click_coeur1() {
	coeur = document.getElementsByClassName('glyphsSpriteHeart__outline__24__grey_9')[1]
	coeur.click()
}
function click_coeur2() {
	coeur = document.getElementsByClassName('glyphsSpriteHeart__filled__24__red_5')[0]
	coeur.click()
}
function click_fleche() {
	fleche = document.getElementsByClassName('coreSpriteRightPaginationArrow')[0]
	fleche.click()
}

function arti() {
	coeur =document.getElementsByClassName('glyphsSpriteHeart__outline__24__grey_9')[1] == true
	for (var i = 0; i < 10; i++) {
		
		if (coeur) {setTimeout(click_coeur1, 3000);}
		else{setTimeout(click_coeur2, 3000);}
			
	}
		}

*/