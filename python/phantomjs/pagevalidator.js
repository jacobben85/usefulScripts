var page = require('webpage').create(),
    system = require('system'),
    t, address, metaData = [], urlList = [];

addToMetaData = function (text) {
    metaData.push(text);
}

addToUrlList = function (text) {
    urlList.push(text);
}

getUrlDomain = function(url) {
    var domain = "http://www.univision.com";

    var match = url.match('^http:\/\/(.*)\.(com|org)/?(.*)');
    if (match.length > 2) {
        domain = match[1] + '.' + match[2];
    }
    var tmp = domain.split('.');
    if (tmp.length > 2) {
        domain = tmp[tmp.length - 2] + '.' + tmp[tmp.length - 1]
    }
    return domain;
};

cleanupUrl = function(url) {
    if (url.indexOf('?') > -1) {
        url = url.split("?")[0];
    }

    if (url.charAt(url.length - 1) === '/') {
        url = url.substr(0, url.length - 1);
    }

    return url;
};

getUrlDomainComplete = function(url) {
    var domain = "http://www.univision.com";

    var match = url.match('^http:\/\/(.*)\.(com|org)/?(.*)');
    if (match.length > 2) {
        domain = 'http://' + match[1] + '.' + match[2];
    }
    return domain;
};

generateResponse = function () {
    var message = "", metadataString = "", urllistString = "";

    while (metaData.length) {
        metadataString = metadataString + "<info>" + metaData.shift() + "</info>";
    }
    metadataString = "<metadata>" + metadataString + "</metadata>";

    while (urlList.length) {
        urllistString = urllistString + "<url>" + urlList.shift() + "</url>";
    }
    urllistString = "<urlList>" + urllistString + "</urlList>";

    message = '<?xml version="1.0"?><reponse>' + metadataString + urllistString + '</reponse>';
    console.log(message);
}

if (system.args.length === 1) {
    addToMetaData('Usage: loadspeed.js <some URL>');
    phantom.exit(1);
} else {
    t = Date.now();
    address = system.args[1];
    page.open(address, function (status) {
        if (status !== 'success') {
            addToMetaData('FAIL to load the address');
        } else {
            t = Date.now() - t;

            var domain = getUrlDomain(address);
            var domainComplete = getUrlDomainComplete(address);
            addToMetaData('Page title is ' + page.evaluate(function () {
                return document.title;
            }));
            addToMetaData('Loading time ' + t + ' msec');

            var links = page.evaluate(function() {
                return [].map.call(document.querySelectorAll('a'), function(link) {
                    return link.getAttribute('href');
                });
            });
            var beingProcessed = "";
            for (var i = 0; i < links.length; i++) {
                
                beingProcessed = links[i];

                if (beingProcessed.charAt(0) === '/') {
                    beingProcessed = domainComplete + beingProcessed;
                }

                if (beingProcessed.indexOf(domainComplete) === 0) {
                    beingProcessed = cleanupUrl(beingProcessed);
                    addToUrlList(beingProcessed);
                }
            }
        }
        generateResponse();
        phantom.exit();
    });
}
