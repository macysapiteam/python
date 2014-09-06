$.ajax({
	//select the service and URI
	url: '/v3/catalog/reviews?productId=77589',
	success: function(data) {
		//do something with your data
		$('body').append('Look at your console in developer tools!')
		console.log(data);
	}
})

