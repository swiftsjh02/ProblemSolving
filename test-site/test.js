var encoder=require('node:punycode')
var http = require('http');
var url = require('url');
var qs = require('querystring');
const { encode } = require('punycode');

var server = http.createServer(function(request, response){
    var _url = request.url;
    var queryData = url.parse(_url, true).query;
    var title = queryData.id
    if(_url == '/'){
      title = 'Welcome';
    }
    if(_url == '/favicon.ico'){
      return response.writeHead(404);
    }
    if(_url == '/greeting'){
      title=queryData.id;
    }
    response.writeHead(200,{'Content-Type':'text/plain; charset=utf8'});
    response.end(title);
}
);
server.listen(80);
console.log('Server is running...');
