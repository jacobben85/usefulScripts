http = require 'http'
fs = require 'fs'

http.createServer (req, res) ->

    fs.readFile "index.html", (err, data) ->
    
      if not err
        res.writeHead 200, {"Content-Type": "text/html"};
        res.write data;
        res.end();
      else
        res.writeHead 404, {"Content-Type": "text/html"};
        res.write "Error loading html";
        res.end();        

.listen(8000, "localhost")

    