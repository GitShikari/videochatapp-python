from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/room/<room_name>')
def room(room_name):
    return render_template('room.html', room_name=room_name)

@app.route('/create_room', methods=['POST'])
def create_room():
    user_name = request.form['name']
    room_name = f"room-{user_name}"  # Unique room name based on user name
    return render_template('invite.html', room_name=room_name)

@socketio.on('signal')
def handle_signal(data):
    room_name = data.get('room')
    if room_name:
        emit('signal', data, room=room_name)
    else:
        emit('signal', data, broadcast=True, include_self=False)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
