/*  global __dirname*/

var connect, serverStatic;

connect = require('connect');

serverStatic = require('serve-static');

connect().use(serverStatic(__dirname)).listen(8000);
