
var express = require('express')
  , app = express.createServer()
  , io = require('socket.io').listen(app);

app.listen(8009);
io.set('log level', 1);
app.use(express.bodyParser());
app.get('/', function (req, res) {
  res.sendfile(__dirname + '/index.html');
});

app.post('/sendstream', function(req, res) {
  //console.log("Got a stream thingie req:"+req.body+" res:"+res);
  //for (param in req.body) {
  //   console.log("param of req is : "+param);
  //   console.log("       "+req.body[param]);
  //}
  io.sockets.volatile.emit('stream', { data:req.body.data });
  res.send("cool.");
});

