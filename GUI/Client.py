import ast
import hashlib
import json
import logging
import select
import socket

import UserPromptGUI, ipEntryGUI
import tkinter as tk

logging.basicConfig(level=logging.DEBUG)

class User:
    def __init__(self, username, password, ip, port):
        self.ip = ip
        self.port = port
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_socket.connect((self.ip, self.port))
        self.success = False  # Whether the User Connection was successful
        self.drawing = 0  # Whether or not we are in drawing mode
        self.changed = 0  # Whether the client name list was updated
        self.client_name_list = []
        # Encypt password for security purposes
        hash_object = hashlib.md5(password.encode())
        md5_hash = hash_object.hexdigest()

        self.my_socket.send(
            ("C" + username + "|" + md5_hash).encode())  # Inquires if the username and password are valid
        logging.info("Checking Client Info")
        confirm = self.my_socket.recv(512).decode().lower()
        logging.info("Client Certificate received: " + confirm)
        if confirm == "yes":
            logging.info("Client is Authentic")
            self.username = username
            self.password = password
            self.success = True
        logging.info("Client Creation Successfull")
        self.my_socket.close()

    def get_connected_Clients(self):
        self.my_socket.send("L".encode())

    def parse_connected_clients(self, clients_string: str):
        clients_string = clients_string[1:]
        logging.info("Clients_string:"+clients_string)
        self.client_name_list = ast.literal_eval(clients_string)
        self.changed = 1

    def inquire_lobby(self, lobby_id):
        # Ask the main server if The lobby exists, and if it does, connect to it
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_socket.connect((self.ip, self.port))
        self.my_socket.send(("I" + str(lobby_id)).encode())
        logging.info("Checking if lobby exists")
        lobby_ip = str(self.my_socket.recv(1024).decode())
        logging.info(lobby_ip)
        logging.info(type(lobby_ip))
        logging.info(lobby_ip is not str(-1))
        self.my_socket.close()
        if lobby_ip != str(-1):
            self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.my_socket.connect((lobby_ip, 5556))
            self.my_socket.send(("U" + self.username).encode())
            confirmation = self.my_socket.recv(1024).decode()
            logging.info("Username sent to server")
            if confirmation == "yes":
                return True
            else:
                return False
        else:
            return False

    def wait_for_lobby(self):
        # Requires Connection to Lobby. Waits until lobby sends "D" for drawing and changes to drawing mode
        self.rlist, wlist, xlist = select.select([self.my_socket], [], [], 0.1)
        for current_socket in self.rlist:
            confirmation = current_socket.recv(1024).decode()
            if confirmation == "D":
                self.drawing = 1


class Lobby:
    def __init__(self, lobby_name, priv_or_publ, client_name, ip, port):
        self.name = lobby_name
        self.security_status = priv_or_publ
        self.client_name = client_name
        self.ip = ip
        self.port = port
        self.users = []
        self.data = []
        self.rlist = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_socket.connect((self.ip, self.port))
        self.my_socket.send("L".encode())
        self.id = self.my_socket.recv(512).decode()
        self.bg_file_destination = ''

        logging.info("Finished making lobby credentials")
        # Setting up the mini server
        self.SERVER_PORT = 5556
        self.SERVER_IP = '0.0.0.0'

        logging.debug("Setting up server...")
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.SERVER_IP, self.SERVER_PORT))
        self.server_socket.listen()
        logging.info("Listening for clients...")
        self.client_sockets = []
        self.messages_to_send = []
        self.connected_users = {}
        self.socket_address_map = {}

    def print_client_sockets(self, client_sockets):
        for i in range(len(client_sockets)):
            logging.debug(client_sockets[i])

    def newclient(self, current_socket: socket.socket, client_sockets):
        if not self.security_status:
            connection, client_address = current_socket.accept()
            self.socket_address_map[connection] = client_address
            connection.send("yes".encode())
            logging.info("New client joined!")
            client_sockets.append(connection)
            self.print_client_sockets(client_sockets)
        else:  # Make a popup for asking
            connection, client_address = current_socket.accept()
            client_username = connection.recv(1024).decode()[1:]
            self.confirmationPopup(client_username, connection, client_address)

    def client_messege(self, current_socket: socket.socket):
        data = current_socket.recv(1024).decode()
        logging.info("Data: " + data)
        logging.info("Sender: " + str(current_socket))
        if data == "":
            logging.info("Connection closed with client")
            self.client_sockets.remove(current_socket)
            self.rlist.remove(current_socket)
            current_socket.close()
        else:
            command = data[0]
            params = data[1:]
            if command == "U":  # A new client has sent us their "U"sername
                socket_address = self.socket_address_map[current_socket]
                self.connected_users[params] = socket_address[0]
                logging.info("User " + params + " Added to user list")
            if command == "L":  # A client requested all the names of all clients connected to us
                current_socket.send(("L" + self.send_names()).encode())
            if command == "D":  # A client drew a drawing, send it to all other clients
                self.update_clients(params)

    def send_names(self):
        user_names = list(self.connected_users.keys())
        user_names.append(self.client_name)
        user_names = list(dict.fromkeys(user_names))
        return str(user_names)

    def get_data(self):
        return self.data

    def update_clients(self, drawing_string):
        drawing = json.loads(drawing_string)
        self.data += drawing
        self.send_to_everyone(drawing_string)

    def check_popup(self, t, current_socket, root, connection_address):
        if t.confirm == 0:  # Lobby manager did not allow the user to join
            current_socket.send("no".encode())
            root.destroy()
            current_socket.close()
        elif t.confirm == 1:  # Lobby manager allowed the user to join
            current_socket.send("yes".encode())
            self.socket_address_map[current_socket] = connection_address
            logging.info("New Client Joined!")
            self.client_sockets.append(current_socket)
            self.print_client_sockets(self.client_sockets)
            socket_address = self.socket_address_map[current_socket]
            self.connected_users[t.username] = socket_address[0]
            logging.info("User " + t.username + " Added to user list")
            root.destroy()
        else:
            root.after(100, lambda: self.check_popup(t, current_socket, root, connection_address))

    def confirmationPopup(self, username, current_socket: socket.socket, connection_address):
        root = tk.Tk()
        t = UserPromptGUI.Toplevel1(username=username, top=root)
        root.after(100, lambda: self.check_popup(t, current_socket, root, connection_address))

    def send_bg_file(self, file_dest):
        """self.bg_file_destination = file_dest
        bg_file = open(self.bg_file_destination, 'rb')
        message = str(bg_file.read())
        length = str(len(message))
        logging.info(length)
        length_of_length = str(len(length)).zfill(4)
        final_message = "B" + length_of_length + length + message
        logging.info("Bg: " + self.bg_file_destination)
        self.send_to_everyone(final_message)"""
        pass

    def one_loop(self):
        logging.info("main looping")
        self.rlist, wlist, xlist = select.select([self.server_socket] + self.client_sockets, [], [], 0.1)
        logging.info("rlist acquired")
        for current_socket in self.rlist:
            if current_socket is self.server_socket:  # new client joins
                self.newclient(current_socket, self.client_sockets)  # create new client
            else:  # what to do with new client
                self.client_messege(current_socket)
        logging.info("responding to clients")
        for message in self.messages_to_send:
            current_socket, data = message
            if current_socket in wlist:
                current_socket.send(data.encode())
                self.messages_to_send.remove(message)

    def exit_protocol(self):
        logging.info("Closing sockets")
        for client_socket in self.client_sockets:
            client_socket.close()
        logging.info("sending archive to server")
        # Remove duplicates from self.data
        new_data = []
        for drawing in self.data:
            if drawing not in new_data:
                new_data.append(drawing)
        new_data.insert(0, [self.name])
        message = json.dumps(new_data)
        length = str(len(message))
        length_of_length = str(len(length)).zfill(4)
        final_message = "F" + length_of_length + length + message
        self.my_socket.send(final_message.encode())
        logging.info("goodbye")

    def send_to_everyone(self, message: str):
        # Sends Message to all clients
        logging.info("Message: "+message+" Sent to Everyone")
        for current_socket in self.client_sockets:
            current_socket.send(message.encode())
