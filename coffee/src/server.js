var http;

http = require('http');

http.createServer(function(request, response) {
  response.writeHead(200, {
    "content-type": "text/html"
  });
  response.write("first coffee script");
  return response.end();
}).listen(8000, 'localhost');

console.log("Server started");
