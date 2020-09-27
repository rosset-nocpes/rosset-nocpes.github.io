//Hook up the tweet display

$(document).ready(function() {
						   
	$(".countdown").countdown({
				date: "28 sep 2020 16:30:00",
				format: "on"
			},
			
			function() {
				// callback function
			});

});	
