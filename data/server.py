import socket
from _thread import *
import sys
import pickle

from . import Player


server = "192.168.1.244"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


players = [Player(0, 0, (255, 0, 0)), Player(300, 300, (0, 255, 0))]


def threaded_client(conn, currentPlayer):
    conn.send(pickle.dumps(players[currentPlayer]))

    reply = ""

    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[currentPlayer] = data

            if not data:
                print("Disconnected")
                break
            else:
                if currentPlayer == 1:
                    reply = players[0]
                else:
                    reply = players[1]

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
