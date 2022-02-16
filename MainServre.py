import select
import logging
import socket
import pickle

SERVER_PORT = 5555
SERVER_IP = '0.0.0.0'

logging.basicConfig(level=logging.DEBUG)


def print_client_sockets(client_sockets):
    for i in range(len(client_sockets)):
        logging.debug(client_sockets[i])


def newclient(current_socket, client_sockets):
    connection, client_address = current_socket.accept()
    logging.info("New client joined!")
    client_sockets.append(connection)
    print_client_sockets(client_sockets)


def client_messege(current_socket: socket.socket):
    command = current_socket.recv(1).decode()  # get the request the client wants us to do
    # TODO: ADD COMMANDS "M" (NEW "M"EMBER, REQUESTED FROM WEBSITE), "F" (END OF LOBBY, GET THE ARCHIVE "F"ILE),
    # TODO: "L" (NEW LOBBY, SEND UNIQUE ID)
    if command == "L":  # A new lobby has just sent this, send back a unique id for it
        current_socket.send(str(lobby_id).zfill(12))


logging.debug("Setting up server...")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()
logging.info("Listening for clients...")
client_sockets = []
messages_to_send = []
# place for parameters

lobby_id = 0  # Will be zfilled to 12 chars for every lobby, then increased by 1.
# This ensures 1,000,000,000,000 unique id's


while True:
    rlist, wlist, xlist = select.select([server_socket] + client_sockets, client_sockets, [])
    for current_socket in rlist:
        if current_socket is server_socket:  # new client joins
            newclient(current_socket, client_sockets)  # create new client
        else:  # what to do with new client
            client_messege(current_socket)

    for message in messages_to_send:
        current_socket, data = message
        if current_socket in wlist:
            current_socket.send(data.encode())
            messages_to_send.remove(message)
