
$( document ).ready(function() {
$( "#scr" ).click(function() {
	$("html, body").animate({
		scrollTop: $("#scratch").offset().top
	}, 300) ;
});

$( "#pyth" ).click(function() {
	$("html, body").animate({
		scrollTop: $("#python").offset().top
	}, 300) ;
});
});
