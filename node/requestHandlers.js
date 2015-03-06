/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


/* global exports, require */
var exec = require("child_process").exec;

function start(response) {
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
function upload(response) {
    response.writeHead(200, {"Content-Type": "text/plain"});
    response.write("Upload Page");
    response.end();
    console.log("Request handler 'upload' was called.");
}

exports.start = start;
exports.upload = upload;