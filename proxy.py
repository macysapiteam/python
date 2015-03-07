from flask import Flask, Response, stream_with_context, request
import requests
import os

app = Flask(__name__, static_url_path='/static')

# This is a basic proxy. Clientside requests should be made to a URI starting with '/api'
@app.route('/api/<path:uri>')
def api(uri):
	requestUri = os.path.join('http://api.macys.com/', uri)
	if request.query_string: 
		requestUri = os.path.join(requestUri, '?' + request.query_string)
	# Change the X-Macys-Webservice-Client-Id to your own
	req = requests.get(requestUri, headers={'Accept':'application/json', 'X-Macys-Webservice-Client-Id': 'Launch2015'}, stream=True)
	return Response(stream_with_context(req.iter_content()), content_type = req.headers['content-type'])

# This serves static files
@app.route('/<path:path>')
def router(path):
	base = os.path.splitext(path)[0]
	return app.send_static_file(path)

# This serves the default page from static/index.html
@app.route('/')
def root():
	return app.send_static_file('index.html')

if __name__ == '__main__':
	app.run();
