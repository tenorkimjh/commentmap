$(document).ready(function(){
    //Handles menu drop down
    $('.dropdown-menu').find('form').click(function (e) {
    	e.stopPropagation();
    });


    $('#category-btn a').on('click', function(){
    	var sel = $(this).data('title');
    	var tog = $(this).data('toggle');
    	$('#'+tog).prop('value', sel);
    	$('#input-form').show()
    	$('a[data-toggle="'+tog+'"]').not('[data-title="'+sel+'"]').removeClass('active').addClass('notActive');
    	$('a[data-toggle="'+tog+'"][data-title="'+sel+'"]').removeClass('notActive').addClass('active');
    })




});

