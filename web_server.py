"""
A Server meant to deal with web clients. This is different from the main server because it requires utilisation of
websocket.
Additionally, I used asyncio for the web server because I could not get it to work without async
Async Explanation: https://www.aeracode.org/2018/02/19/python-async-simplified/
"""
import json
import os
import socket
import threading

import websockets
import asyncio
import pickle


class webserver:

    def check_client_info(self, params):
        print("Client params: " + str(params))
        client_username = params[0]
        c_password = params[1]

        client_infos = open("client_info.txt", "rb")
        client_database = pickle.load(client_infos)
        client_infos.close()
        print("Client Database: " + str(client_database))
        if client_username not in client_database:
            print("Client does not exist")
            return "Cn"
        else:
            if client_database[client_username] == c_password:
                print("Client exists")
                return "Cy"
            else:
                print("Client does not exist")
                return "Cn"

    def create_account(self, user_details):
        print("Client details: " + str(user_details))
        new_username = user_details[0]
        new_password = user_details[1]
        self.my_socket.send(("M" + new_username + "|" + new_password).encode())
        return "S"

    async def respond_to_web_message(self, message):
        print(message)
        directive = message[0]
        print(directive)
        if directive == "C":  # A client is trying to log in, check if He exists in the Database
            params = message[1:].split("|")
            print("params: " + str(params))
            print("Checking client info")
            return self.check_client_info(params)
        if directive == "M":  # A client wants to "M"ake an account, create it
            user_details = message[1:].split("|")
            print("User details: "+ str(user_details))
            print("Creating account")
            return self.create_account(user_details)
        if directive == "D":  # A client asked us for the name of every drawing in the "D"atabate directory, send it
            file_name_list = os.listdir("database")
            print(file_name_list)
            return "D"+json.dumps(file_name_list)
        if directive == "V":  # A client asked us for a file, send it
            file_name = message[1:]
            file = open("database/"+file_name, 'r')
            file_string = file.read()
            file_string = file_string.replace("'", '"')
            print(file_string)
            file.close()
            return "V" + str(file_string)
        else:
            return "message: " + message + ". Received"

    async def handler(self, websocket, path):
        async for request in websocket:
            print("request: " + request)
            response = await self.respond_to_web_message(request)
            await websocket.send(response)

    def __init__(self, main_server_ip_address):
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_socket.connect((main_server_ip_address, 5555))
        start_server = websockets.serve(self.handler, '0.0.0.0', 5678)
        print("Starting server")
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()


def main():
    main_server_ip = input("Please enter server IP")
    my_web_server = webserver(main_server_ip)


if __name__ == '__main__':
    main()
