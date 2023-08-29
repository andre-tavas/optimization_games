from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('command')
def handle_command(data):
    # Lógica para interpretar o comando e atualizar o jogo
    key = data['key']
    socketio.emit('command', {'key': key}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
