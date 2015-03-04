#Macys.com API Sample Starter with local proxy
Welcome! Follow these directions to set up a local proxy on your machine for the macys.com API

## Instructions
* Make sure you have Python installed
* `cd` to this project directory
* run `sh -x install.sh`(this will install all dependencies and start the server)
* Go to http://localhost:5000

## Local server
### To start
```Shell
python proxy.py
```

### To kill
Ctrl + C

## To edit
* Make changes in the `static/` directory
* An example ajax call to the macys.com API is under static/js/main.js
* If you'd like to make AJAX calls through this proxy, here is an example:

```javascript
$.ajax({
	//use the api/ route
	url: 'api/v3/catalog/reviews?productId=77589',
	success: function(data) {
		//do something with your data
		console.log(data);
	}
})
```

## Credits
* Based off of this example <a href="http://flask.pocoo.org/snippets/118/">http://flask.pocoo.org/snippets/118/</a>
* More on Flask <a href="http://flask.pocoo.org/">http://flask.pocoo.org/</a>
