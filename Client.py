import hashlib
import logging
import select
import socket

logging.basicConfig(level=logging.DEBUG)
ip = '127.0.0.1'
port = 5555

class User:
    def __init__(self, Username, Password):
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_socket.connect((ip, port))
        self.success = False  # Whether the User Connection was successful

        # Encypt password for security purposes
        hash_object = hashlib.md5(Password.encode())
        md5_hash = hash_object.hexdigest()

        self.my_socket.send(("C"+Username+"|"+md5_hash).encode())  # Inquires if the username and password are valid
        print("Checking Client Info")
        confirm = self.my_socket.recv(512).decode().lower()
        print("Client Certificate received: " + confirm)
        if confirm == "yes":
            print("Client is Authentic")
            self.Username = Username
            self.Password = Password
            self.success = True
        print("Client Creation Successfull")
        self.my_socket.close()



class Lobby:
    def __init__(self, lobby_name):
        self.name = lobby_name
        self.data = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_socket.connect((ip, port))
        self.my_socket.send("L")
        self.id = self.my_socket.recv(512).decode()

        # Setting up the mini server
        self.SERVER_PORT = 5555
        self.SERVER_IP = '0.0.0.0'

        logging.debug("Setting up server...")
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.SERVER_IP, self.SERVER_PORT))
        self.server_socket.listen()
        logging.info("Listening for clients...")
        self.client_sockets = []
        self.messages_to_send = []
        self.main_loop()

    def print_client_sockets(self, client_sockets):
        for i in range(len(client_sockets)):
            logging.debug(client_sockets[i])

    def newclient(self, current_socket, client_sockets):
        connection, client_address = current_socket.accept()
        logging.info("New client joined!")
        client_sockets.append(connection)
        self.print_client_sockets(client_sockets)

    def client_messege(self, current_socket: socket.socket):
        pass
        # TODO: ADD RECEIVING DRAWINGS AND ADDING TO DATA USING PROCEDURE FOR LONG MESSAGE RECEIVES

    def main_loop(self):
        while True:
            rlist, wlist, xlist = select.select([self.server_socket] + self.client_sockets, self.client_sockets, [])
            for current_socket in rlist:
                if current_socket is self.server_socket:  # new client joins
                    self.newclient(current_socket, self.client_sockets)  # create new client
                else:  # what to do with new client
                    self.client_messege(current_socket)

            for message in self.messages_to_send:
                current_socket, data = message
                if current_socket in wlist:
                    current_socket.send(data.encode())
                    self.messages_to_send.remove(message)
