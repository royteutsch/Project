import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
class lobby():
    def __init__(self, lobby_name):
        self.name = lobby_name
        self.data = []




my_socket.connect(('127.0.0.1', 8564))
choice = input("Enter e for existing member, or n for new member")
if choice == "e":
    username = input("Please enter your username")
    # TODO: ADD INQUIRY WITH MAIN SERVER FOR EXISTENCE OF USERNAME IN DATABASE
    password = input("Please enter your password")
    # TODO: ADD INQUIRY WITH MAIN SERVER IF PASSWORD IS CORRECT
    # TODO: ADD RESPONSES
    # TODO: ADD CONNECTION TO CLIENT
if choice == "n":

    # TODO: ADD FORWARDING TO MEMBER CREATION IN WEBSITE
# The client is assumed to be connected to a member from this point forth

choice = input("Enter c to connect to an existing lobby, or m to make your own")
if choice == "c":
    lobby_name = input("Please enter a name for your lobby")
    l = lobby(lobby_name)
