var http = require('http');

var lastOpen = 0;

getLastUpdate();

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.end('<h1>Instagram Console:</h1>" + " <br> <p style="color:red;">Last Opened On: ' + lastOpen + "</p>" + "<br>");
}).listen(8080); 

function getLastUpdate(){

    var fs = require('fs');

    fs.readFile('lastdate.txt', 'utf8', function(err, data) {
        if (err) throw err;
        console.log(data);
        lastOpen = data;
    });

}