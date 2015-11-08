/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* global exports */

function route(handle, pathname, response, postData) {
    console.log("About to route a request for " + pathname); 
    if (typeof handle[pathname] === 'function') {
        
        handle[pathname](response, postData);
        
    } else {
        response.writeHead(404, {"Content-Type": "text/plain"});
        response.write("No request handler found for " + pathname);
        response.end();
    }
}

exports.route = route;