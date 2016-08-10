alert("Welcome! You may need pygame in order to view some projects.");
function imageBigger(x) {
	var Screenshot1 = document.getElementById(x);
	Screenshot1.style.width='400px';Screenshot1.style.height='280px';
}
function imageSmaller(x) {
	var Screenshot1 = document.getElementById(x);
	Screenshot1.style.width='200px';Screenshot1.style.height='140px';
}

function showaboutme() {
	if ($(".hidden-button").hasClass("shown"))
		$(".hidden-button").removeClass("shown").fadeOut();
	else
		$(".hidden-button").addClass("shown").fadeIn()
}


