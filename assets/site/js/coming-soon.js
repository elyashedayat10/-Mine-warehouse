/* Website Launch Date */ 
var WebsiteLaunchDate = new Date();
monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
WebsiteLaunchDate.setMonth(WebsiteLaunchDate.getMonth() + 1);
WebsiteLaunchDate =  WebsiteLaunchDate.getDate() + " " + monthNames[WebsiteLaunchDate.getMonth()] + " " + WebsiteLaunchDate.getFullYear(); 
/* Website Launch Date END */ 
/* Set Footer Section */	
function setFooterSection()
{
	$windowWidth = $(window).width();
	
	if($windowWidth <= 1920)
	{
		if($('.f-ele-m')[0])
		{
			$centerDiv = $('.f-ele-m');
			$marginVal  = $centerDiv.attr('dez-top-pos') ? $centerDiv.attr('dez-top-pos') : 0  ;
			$position  = $centerDiv.attr('dez-position') ? $centerDiv.attr('dez-position') : true  ;
			//alert($position);
			//alert($marginVal);
			$windowHeight = $(window).height();
			$centerDivHeight = $centerDiv.height();
			$marginHeight = ($windowHeight - $centerDivHeight) / 2 ;
			$marginHeight = $marginHeight - ($marginHeight * $marginVal / 100);
			//alert($marginVal);
			
			//alert($windowWidth);
			if(($windowWidth < 460 || $windowWidth > 700) && $position == true)
			{
				//alert('dfgdfg');
				$('.f-ele-m').css("position", 'fixed');
			}
		
			if($position == true )
			{
				$('.f-ele-m').css("margin-top", '0');
				$('.f-ele-m').css("top", $marginHeight);	
			}
			else{
				$('.f-ele-m').css("margin-top", $marginHeight);
				$('.f-ele-m').css("margin-bottom", $marginHeight);
			}
			
			$('.f-ele-m').css("padding", '0 15px ');
			$('.f-ele-m').css("left", '0');

		}
	}	
}
/* countdown */

	$(document).ready(function() {
      $('.countdown').countdown({date: WebsiteLaunchDate+' 23:5'}, function() {
        $('.countdown').text('وبسایت راه اندازی شد');
      });
    });
	
/* countdown End */	

function openNav() {
	
	$('.openbtn').on('click',function(e){
		e.preventDefault();
		if($('#mySidenav').length > 0)
		{
			document.getElementById("mySidenav").style.right = "0";
		}
	})

	$('.openbtnhold').on('click', function (e) {
		e.preventDefault();
		if ($('#mySidenavHold').length > 0) {
			document.getElementById("mySidenavHold").style.right = "0";
		}
	})

	$('.openbtnvisit').on('click', function (e) {
		e.preventDefault();
		if ($('#mySidenavVisit').length > 0) {
			document.getElementById("mySidenavVisit").style.right = "0";
		}
	})

	$('.openbtnsample').on('click', function (e) {
		e.preventDefault();
		if ($('#mySidenavSample').length > 0) {
			document.getElementById("mySidenavSample").style.right = "0";
		}
	})
}

function closeNav() {
    
	$('.closebtn').on('click',function(e){
		e.preventDefault();
		if($('#mySidenav').length > 0)
		{
			document.getElementById("mySidenav").style.right = "-1020px";
		}
	})


	$('.closebtnhold').on('click',function(e){
		e.preventDefault();
		if($('#mySidenavHold').length > 0)
		{
			document.getElementById("mySidenavHold").style.right = "-1020px";
		}
	})

	$('.closebtnvisit').on('click',function(e){
		e.preventDefault();
		if($('#mySidenavVisit').length > 0)
		{
			document.getElementById("mySidenavVisit").style.right = "-1020px";
		}
	})

	$('.closebtnsample').on('click',function(e){
		e.preventDefault();
		if($('#mySidenavSample').length > 0)
		{
			document.getElementById("mySidenavSample").style.right = "-1020px";
		}
	})
}

/* Scroll */
	(function($){
		$(window).on("load",function(){
			/* all available option parameters with their default values */
			$(".content").mCustomScrollbar({
				setWidth:false,
				setHeight:false,
				axis:"y",
			});
		});
	})(jQuery);
	
// function([string1, string2],target id,[color1,color2])
 function dezText(words, id) {
		'use strict';
	if($('#'+id).length > 0)
	{
		var visible = true;
        var letterCount = 1;
        var x = 1;
        var waiting = false;
        var target = document.getElementById(id);
        window.setInterval(function() {

            if (letterCount === 0 && waiting === false) {
                waiting = true;
                target.innerHTML = words[0].substring(0, letterCount);
                window.setTimeout(function() {
                    var usedWord = words.shift();
                    words.push(usedWord);
                    x = 1;
                    letterCount += x;
                    waiting = false;
                }, 500)
            } else if (letterCount === words[0].length + 1 && waiting === false) {
                waiting = true;
                window.setTimeout(function() {
                    x = -1;
                    letterCount += x;
                    waiting = false;
                }, 1000)
            } else if (waiting === false) {
                target.innerHTML = words[0].substring(0, letterCount);
                letterCount += x;
            }
        }, 70)
	}	
}
/*################	End OF Function List ###################################*/
/* Document.ready Start */	
jQuery(document).ready(function() {
    'use strict';
	
	setFooterSection(); 
	
	closeNav();
	
	openNav();
	
	dezText(['به زودی...، صبور باشید', 'به زودی...، صبور باشید'], "text");
	
});
/* Document.ready END */
/* Loading */
	jQuery(window).load(function() {
		setTimeout(function(){
			jQuery('#loading-area').remove();
		}, 0);
	});
/* Loading End */