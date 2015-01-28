var webPage = require('webpage');
var page = webPage.create();

page.onResourceReceived = function(response) {
  console.log('Response (#' + response.id + ', stage "' + response.stage + '"): ' + JSON.stringify(response));
};

page.render("http://nfl.univision.com/feed/sports/american-football/nfl/2014/event-nfl-56499.xml");