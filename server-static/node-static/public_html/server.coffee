###  global __dirname ###

connect = require 'connect'
serverStatic = require 'serve-static'
connect().use(serverStatic(__dirname)).listen(8000)