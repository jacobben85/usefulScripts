/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


/* global exports, require */
var exec = require("child_process").exec;
var querystring = require("querystring");

function start_old(response) {
    exec("ls -lah", function (error, stdout, stderr) { 
        response.writeHead(200, {"Content-Type": "text/plain"});
        response.write(stdout);
        response.end();
        console.log(stdout);
        console.log(error);
        console.log(stderr);
    });
    console.log("Request handler 'start' was called.");
}
function upload_old(response) {
    response.writeHead(200, {"Content-Type": "text/plain"});
    response.write("Upload Page");
    response.end();
    console.log("Request handler 'upload' was called.");
}
function start(response, postData) {
    var body = '<html>'+
            '<head>'+
            '<meta http-equiv="Content-Type" content="text/html; '+ 
            'charset=UTF-8" />'+
            '</head>'+
            '<body>'+
            '<form action="/upload" method="post">'+
            '<textarea name="text" rows="20" cols="60"></textarea>'+ 
            '<input type="submit" value="Submit text" />'+ 
            '</form>'+
            '</body>'+
            '</html>';
    response.writeHead(200, {"Content-Type": "text/html"});
    response.write(body);
    response.end();
}
function upload(response, postData) {
    response.writeHead(200, {"Content-Type": "text/plain"});
    response.write(querystring.parse(postData).text);
    response.end();
    console.log("Request handler 'upload' was called.");
}

exports.start = start;
exports.upload = upload;