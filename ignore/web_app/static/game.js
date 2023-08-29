document.addEventListener('DOMContentLoaded', function () {
    var canvas = document.getElementById('gameCanvas');
    var context = canvas.getContext('2d');

    var socket = io.connect('http://' + document.domain + ':' + location.port);

    // // Função para enviar comandos do teclado para o servidor
    // function sendCommand(key) {
    //     socket.emit('command', { key: key });
    // }

    // Escuta eventos do teclado e envia os comandos para o servidor
    document.addEventListener('keydown', function(event) {
        if (event.key === 'ArrowUp' || event.key === 'ArrowDown' || event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
            socket.emit('keypress', { key: event.key });
        }
    });

    socket.on('connect', function() {
        console.log('Connected to server');
    });
});
