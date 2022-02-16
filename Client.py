import logging
import select
import socket
import sys
import webbrowser
import tkinter
from tkinter import *
from tkinter import ttk

logging.basicConfig(level=logging.DEBUG)


class Lobby:
    def __init__(self, lobby_name):
        self.name = lobby_name
        self.data = []
        my_socket.send("L")
        self.id = my_socket.recv(512).decode()

        # Setting up the mini server
        SERVER_PORT = 5555
        SERVER_IP = '0.0.0.0'

        logging.debug("Setting up server...")
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((SERVER_IP, SERVER_PORT))
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
        # TODO: ADD RECEIVING DRAWINGS AND ADDING TO DATA USING PROCEDURE FOR LONG MESSAGE RECEIVES
        pass

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


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#my_socket.connect(('127.0.0.1', 8564))

# GUI
root = tkinter.Tk()

style = ttk.Style()
style.theme_settings("default", {
   "TCombobox": {
       "configure": {"padding": 5},
       "map": {
           "background": [("active", "green2"),
                          ("!disabled", "green4")],
           "fieldbackground": [("!disabled", "green3")],
           "foreground": [("focus", "OliveDrab1"),
                          ("!disabled", "OliveDrab2")]
       }
   }
})

ttk.Combobox().pack()

root.mainloop()

choice = input("Enter e for existing member, or n for new member").lower()
if choice == "e":
    username = input("Please enter your username")
    # TODO: ADD INQUIRY WITH MAIN SERVER FOR EXISTENCE OF USERNAME IN DATABASE
    password = input("Please enter your password")
    # TODO: ADD INQUIRY WITH MAIN SERVER IF PASSWORD IS CORRECT
    # TODO: ADD RESPONSES
    # TODO: ADD CONNECTION TO CLIENT
if choice == "n":
    webbrowser.open("www.google.com")
    # TODO: ADD FORWARDING TO MEMBER CREATION IN WEBSITE
else:
    print("Invalid Choice, Goodbye")
    sys.exit()
# The client is assumed to be connected to a member from this point forth

choice = input("Enter c to connect to an existing lobby, or m to make your own")
if choice == "c":
    lobbyName = input("Please enter a name for your lobby")
    l = Lobby(lobbyName)
