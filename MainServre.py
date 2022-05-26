import json
import os
import select
import logging
import socket
import pickle
from typing import List


class Server:

    def __init__(self):
        self.SERVER_PORT = 5555
        self.SERVER_IP = '0.0.0.0'
        self.socket_address_map = {}
        logging.basicConfig(level=logging.DEBUG)

        logging.debug("Setting up server...")
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.SERVER_IP, self.SERVER_PORT))
        server_socket.listen()
        logging.info("Listening for clients...")
        self.client_sockets = []
        self.active_lobbies = {}  # The dict is structured as {lobby ID : lobby IP}
        self.num_of_unnamed_files = 0
        messages_to_send = []
        # place for parameters

        self.lobby_id = 0  # Will be zfilled to 12 chars for every lobby, then increased by 1.
        # This ensures 1,000,000,000,000 unique id's

        while True:
            self.rlist, wlist, xlist = select.select([server_socket] + self.client_sockets, self.client_sockets, [])
            for current_socket in self.rlist:
                if current_socket is server_socket:  # new client joins
                    self.newclient(current_socket, self.client_sockets)  # create new client
                else:  # what to do with new client
                    print(str(current_socket)+": Client Requested Something")
                    self.client_messege(current_socket)

            for message in messages_to_send:
                current_socket, data = message
                if current_socket in wlist:
                    print("Analysing Client")
                    current_socket.send(data.encode())
                    messages_to_send.remove(message)

    def print_client_sockets(self, client_sockets):
        for i in range(len(client_sockets)):
            logging.debug(client_sockets[i])

    def newclient(self, current_socket, client_sockets):
        connection, client_address = current_socket.accept()

        self.socket_address_map[connection] = client_address

        logging.info("New client joined!")
        client_sockets.append(connection)
        self.print_client_sockets(client_sockets)

    def create_account(self, params):
        c_username = params[0]
        c_password = params[1]

        client_infos = open("client_info.txt", "rb")
        client_database = pickle.load(client_infos)
        print("Client Database: " + str(client_database))
        if c_username not in client_database:  # we will create an account only when the name is not taken
            client_database[c_username] = c_password
            client_infos.close()
            client_infos = open("client_info.txt", "wb")
            pickle.dump(client_database, client_infos)
        client_infos.close()

    def check_client_info(self, params, client):
        print("Client params: " + str(params))
        c_username = params[0]
        c_password = params[1]

        client_infos = open("client_info.txt", "rb")
        client_database = pickle.load(client_infos)
        client_infos.close()
        print("Client Database: " + str(client_database))
        if c_username not in client_database:
            print("Client does not exist")
            client.send("no".encode())
        else:
            if client_database[c_username] == c_password:
                print("Client exists")
                client.send("yes".encode())
            else:
                print("Client does not exist")
                client.send("no".encode())

    def client_messege(self, current_socket: socket.socket):
        command = current_socket.recv(1).decode()  # get the request the client wants us to do
        print("command: " + str(command))
        if command == "":  # Client wants to leave
            print("Connection closed with client")
            self.client_sockets.remove(current_socket)
            self.rlist.remove(current_socket)
            current_socket.close()
        else:
            directive = command
            if directive == "M":  # The web server asked us to Make a new account
                params = current_socket.recv(1024).decode().split("|")
                print("new user params: " + str(params))
                print("creating account")
                self.create_account(params)
            if directive == "F":  # A lobby has just ended, create an archive file
                length_of_lengths = current_socket.recv(4).decode()
                message_length = int(current_socket.recv(int(length_of_lengths)).decode())
                temp_name = "database/" + str(self.num_of_unnamed_files) + ".txt"
                self.num_of_unnamed_files += 1
                soon_to_be_file = ""
                f = open(temp_name, 'wb')
                f.write(''.encode())
                f.close()
                f = open(temp_name, 'ab')
                while not message_length == 0:
                    if message_length <= 9999:
                        data = current_socket.recv(message_length).decode()
                        soon_to_be_file += data
                        f.write(data.encode())
                        break
                    data = current_socket.recv(9999).decode()
                    soon_to_be_file += data
                    f.write(data.encode())
                    print("handling...")
                    message_length -= 9999
                f.close()
                self.handle_file(temp_name)
            if directive == "L":  # A new lobby has just sent this, send back a unique id for it
                current_socket.send(str(self.lobby_id).zfill(12).encode())
                socket_address = self.socket_address_map[current_socket]
                print(socket_address)
                self.active_lobbies[str(self.lobby_id).zfill(12)] = socket_address[0]
                self.lobby_id += 1
            if directive == "C":  # A client is trying to log in, check if He exists in the Database
                params = current_socket.recv(1024).decode().split("|")
                print("params: " + str(params))
                print("Checking client info")
                self.check_client_info(params, current_socket)
            if directive == "I":  # Check if the lobby exists, if it does, send the ip address. If not, send "-1"
                params = current_socket.recv(1024).decode()
                print(params)
                print(self.active_lobbies)
                if params in self.active_lobbies:
                    current_socket.send(self.active_lobbies[params].encode())
                else:
                    current_socket.send("-1".encode())

    def handle_file(self, temp_file_name):
        """
        Renames the file to an appropriate name and adds \n after each object in the list
        :param temp_file_name: The temporary name of the file in question, will be renamed to its entered name
        """
        file = open(temp_file_name, 'r')
        list_string = file.read()
        file.close()
        drawing_list: List = json.loads(list_string)
        print(drawing_list)
        os.rename(temp_file_name, "database/" + str(drawing_list[0][0]) + ".txt")
        self.num_of_unnamed_files -= 1
        file = open("database/" + str(drawing_list[0][0]) + ".txt", 'w')

        file.write(f"{drawing_list[0]}")
        for drawing in drawing_list[1:]:
            file.write(f", \n{str(drawing)}")
        file.close()

def main():
    server = Server()


if __name__ == '__main__':
    main()
