$(function(){
    $.widget( "custom.iconselectmenu", $.ui.selectmenu, {
    	_renderItem: function( ul, item ) {
    		var li = $( "<li>", { text: item.label } );
 
      		if ( item.disabled ) {
        		li.addClass( "ui-state-disabled" );
        	}
 
        	$( "<span>", {
        		style: item.element.attr( "data-style" ), "class": "ui-icon " + item.element.attr( "data-class" )
        	})
        		.appendTo( li );
 
        	return li.appendTo( ul );
      	}
    });
    
    $( "#sports" )
    .iconselectmenu()
    .iconselectmenu( "menuWidget")
    .addClass( "ui-menu-icons avatar" );
});

$('.form_date').datetimepicker({
    weekStart: 1,
    todayBtn:  1,
    autoclose: 1,
    todayHighlight: 1,
    startView: 2,
    minView: 2,
    forceParse: 0
});

$('.form_time').datetimepicker({
    weekStart: 1,
    todayBtn:  1,
    autoclose: 1,
    todayHighlight: 1,
    startView: 1,
    minView: 0,
    maxView: 1,
    forceParse: 0
});