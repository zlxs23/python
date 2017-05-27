def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	text = b'''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>This is worderful</title>
</head>
<body>
	<h1>This is h1</h1>
	<style type="text/css">
		h1{
			color: red;
		}
	</style>
</body>
</html>'''
	return [text]