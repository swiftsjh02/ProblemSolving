//계산기 서버 만드는 코드
var http = require('http');
var url = require('url');
var qs = require('querystring');

var server = http.createServer(function(request, response){
    var _url = request.url;
    var queryData = url.parse(_url, true).query;
    var title = queryData.id;
    if(_url == '/'){
      title = 'Welcome';
    }
    if(_url == '/favicon.ico'){
      return response.writeHead(404);
    }
    response.writeHead(200);
    response.end(qs.parse(queryData.id));
}
);
server.listen(80);
console.log('Server is running...');

