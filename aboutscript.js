
$( document ).ready(function() {
$( "#wh" ).click(function() {
	$("html, body").animate({
		scrollTop: $("#who").offset().top
	}, 300) ;
});

$( "#wha" ).click(function() {
	$("html, body").animate({
		scrollTop: $("#what").offset().top
	}, 300) ;
});

$( "#whe" ).click(function() {
	$("html, body").animate({
		scrollTop: $("#where").offset().top
	}, 300) ;
});
});
