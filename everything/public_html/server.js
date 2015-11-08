var fs, http;

http = require('http');

fs = require('fs');

http.createServer(function(req, res) {
  return fs.readFile("index.html", function(err, data) {
    if (!err) {
      res.writeHead(200, {
        "Content-Type": "text/html"
      });
      res.write(data);
      return res.end();
    } else {
      res.writeHead(404, {
        "Content-Type": "text/html"
      });
      res.write("Error loading html");
      return res.end();
    }
  });
}).listen(8000, "localhost");
