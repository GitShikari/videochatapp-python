from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room
import string
import random

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/room/<room_name>')
def room(room_name):
    return render_template('room.html', room_name=room_name)

@app.route('/create_room', methods=['POST'])
def create_room():
    bithash = ''.join(random.choices(string.ascii_letters,k=32))
    user_name = request.form['name']
    room_name = f"room-{user_name}-{bithash}"  # Unique room name based on user name
    return render_template('invite.html', room_name=room_name)

@socketio.on('join')
def handle_join(data):
    room_name = data['room']
    join_room(room_name)
    print(f"User {request.sid} joined room {room_name}")

@socketio.on('leave')
def handle_leave(data):
    room_name = data['room']
    leave_room(room_name)
    print(f"User {request.sid} left room {room_name}")

@socketio.on('signal')
def handle_signal(data):
    room = data.get('room')  # Ensure room is always provided
    if not room:
        print('Error: Room name is missing in signal data')
        return
    emit('signal', data, room=room, broadcast=True, include_self=False)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
