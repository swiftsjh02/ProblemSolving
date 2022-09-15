//make server listen on port 80



var fs = require('fs');
var index = fs.readFileSync('index.html');
//res.end(index);


var http = require('http');
var server = http.createServer(function(req, res) {
    res.writeHead(200);
    res.end("hello world");
    res.end(index);

    });
server.listen(8080);

