http = require 'http'

http.createServer (request, response) -> 
    response.writeHead 200, {"content-type": "text/html"};
    response.write("first coffee script");
    response.end();
  
.listen(8000, 'localhost')

console.log "Server started"
  