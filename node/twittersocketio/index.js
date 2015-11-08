/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


// Loading required modules
var http = require('http'),
	io = require('socket.io'),
	twitter = require('./twitter');
 
var SERVER_PORT = 8000,
    TWITTER_LOGIN = 'testing',
    TWITTER_PASSWORD = 'testing*',
    TWITTER_TOPICS = 'WsN_Paris,zenika';
 
// Creating HTTP ServerWhat's Next ?
server = http.createServer();
 
// Starting the server
server.listen(SERVER_PORT);
 
// Attaching Socket.IO to the HTTP Server
var socket = io.listen(server);
 
console.log('Server running on port : ' + SERVER_PORT);
 
// Instantiating our tracker
var tracker = new twitter.TwitterTracker(TWITTER_LOGIN, TWITTER_PASSWORD, TWITTER_TOPICS);
 
// Start tracking and waiting for 'tweet' events from our tracker.
tracker.track().on('tweet', function(tweet){
 
        // Print out the tweet
        console.log('New tweet from :"' + tweet.user.screen_name + '" -> ' + tweet.text);
 
        // Using the socket provided by Socket.IO to broadcast the new tweet to all the clients.
	socket.broadcast(
		// To save bandwich we send only the tweet parts we are interested in.
		JSON.stringify( 
			{ 	id : tweet.id, 
				user : tweet.user.screen_name, 
				text : tweet.text, 
				picture : tweet.user.profile_image_url
			}
		)
	);
});
