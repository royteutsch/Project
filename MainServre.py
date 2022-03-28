import select
import logging
import socket
import pickle


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

    def check_client_info(self, params, client):
        print("Client params: " + str(params))
        cUsername = params[0]
        cPassword = params[1]

        client_infos = open("client_info.txt", "rb")
        client_database = pickle.load(client_infos)
        print("Client Database: " + str(client_database))
        if cUsername not in client_database:
            print("Client does not exist")
            client.send("no".encode())
        else:
            if client_database[cUsername] == cPassword:
                print("Client exists")
                client.send("yes".encode())
            else:
                print("Client does not exist")
                client.send("no".encode())

    def client_messege(self, current_socket: socket.socket):
        command = current_socket.recv(1024).decode()  # get the request the client wants us to do
        print("command: " + str(command))
        if command == "":  # Client wants to leave
            print("Connection closed with client")
            self.client_sockets.remove(current_socket)
            self.rlist.remove(current_socket)
            current_socket.close()
        else:
            directive = command[0]
            print("directive: " + directive)
            command = command[1:]
            print("command: " + command)
            # TODO: ADD COMMANDS "M" (NEW "M"EMBER, REQUESTED FROM WEBSITE), "F" (END OF LOBBY, GET THE ARCHIVE "F"ILE),
            # TODO: "I" (A USER WANTS TO CONNECT TO A LOBBY, NOTIFY THE LOBBY, IF IT EXISTS, CHECK THROUGH LOBBY "I"D)
            if directive == "L":  # A new lobby has just sent this, send back a unique id for it
                current_socket.send(str(self.lobby_id).zfill(12).encode())
                socket_address = self.socket_address_map[current_socket]
                print(socket_address)
                self.active_lobbies[str(self.lobby_id).zfill(12)] = socket_address[0]
                self.lobby_id += 1
            if directive == "C":  # A client is trying to log in, check if He exists in the Database
                params = command.split("|")
                print("params: " + str(params))
                print("Checking client info")
                self.check_client_info(params, current_socket)
            if directive == "I":  # Check if the lobby exists, if it does, send the ip address. If not, send "-1"
                print(command)
                print(self.active_lobbies)
                if command in self.active_lobbies:
                    current_socket.send(self.active_lobbies[command].encode())
                else:
                    current_socket.send("-1".encode())

def main():
    server = Server()


if __name__ == '__main__':
    main()
