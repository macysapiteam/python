$.ajax({
	//select the service and URI
	url: 'http://origin-api.macys.com/v3/catalog/reviews?productId=77589',
	//set headers with your key and select json
	headers: {
		'Accept':'application/json',
		'X-Macys-Webservice-Client-Id': 'neohack14'
	},
	success: function(data) {
		//do something with your data
		$('body').append('Look at your console in developer tools!')
		console.log(data);
	}
})

