function changeBackground(element) {
	$(document.body).css('background-image', 'url(arena/' + element.id + '.jpg)');
}

function chooseNinja(color) {
	
}

$( document ).ready(function() {
    $('.button').on('mouseover', function() {
    	changeBackground(this);
    });

    $('.button').on('click', function() {
    	changeBackground(this);
    	$('#select-backgrounds').css('display', 'none');
    	$('#select-players').css('display', 'block');
    })
});	