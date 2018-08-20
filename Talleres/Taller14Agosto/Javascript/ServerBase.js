

var express = require('express')
var app = express();
var server = require('http').Server(app);
var io = require('socket.io')(server);


//importo las operaciones que necesito
var operaciones = require('./operaciones');


app.get('/', function(req, res){
  res.sendFile  (__dirname + '/client.html');
});



io.on('connection', function(socket){
  console.log('a user connected');
  socket.on('operar', function(msg){
    console.log('message: ' + msg);


    io.emit('resultado', "esta es una prueba de recepcion" + msg);
  });
});


server.listen(3009, function(){
  console.log('listening on *:3009');
});
