//Hook up the tweet display

$(document).ready(function() {
						   
	$(".countdown").countdown({
				date: "30 aug 2020 18:30:00",
				format: "on"
			},
			
			function() {
				// callback function
			});

});	