const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);

// Serve html main file
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// Websockets events
io.on('connection', (socket) => {
    console.log('new connection');
    socket.on('disconnect', () => {
        console.log('user disconnected');
    });
    socket.on('temp-hum-data', data => {
        io.emit('temp-hum-data', data);
        console.log('temp-hum-data recieved: ' + data);
    });
});

// Run server
server.listen(3000, () => {
  console.log('listening on *:3000');
});
