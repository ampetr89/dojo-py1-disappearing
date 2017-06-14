
function draw_img(cities, IMG_PATH, caption=true){
	
	for(var city in cities){
		cityname = cities[city]

		$('main').append('<div class="fig-container" city="'+city+'"></div>')
		
		$('.fig-container[city="'+city+'"]').append('<div class="img-container" city="'+city+'"></div>');
		img_src = IMG_PATH.replace('CITY', city);
		$('.img-container[city="'+city+'"]').append('<a href="/cities/'+city+'"><img src="'+img_src+'" city="'+city+'"></a>');

		if(caption){
			$('.fig-container[city="'+city+'"]').append('<p>'+cityname+'</p>');
		}
	}
}

function img_mousover(){
	$(this).fadeTo(200, .6);
	$(this).parent().parent().css('outline', '3px gray solid');
}

function img_mousout(){
	$(this).fadeTo(300, 1);
	$(this).parent().parent().css('outline', '2px black solid');
}
