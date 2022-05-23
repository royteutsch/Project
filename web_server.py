"""
A Server meant to deal with web clients. This is different from the main server because it requires utilisation of
websocket.
Additionally, I used asyncio for the web server because I could not get it to work without async
Async Explanation: https://www.aeracode.org/2018/02/19/python-async-simplified/
"""
import websockets
import asyncio
import pickle

class webserver:

    def check_client_info(self, params):
        print("Client params: " + str(params))
        cUsername = params[0]
        cPassword = params[1]

        client_infos = open("client_info.txt", "rb")
        client_database = pickle.load(client_infos)
        print("Client Database: " + str(client_database))
        if cUsername not in client_database:
            print("Client does not exist")
            return "Cn"
        else:
            if client_database[cUsername] == cPassword:
                print("Client exists")
                return "Cy"
            else:
                print("Client does not exist")
                return "Cn"

    async def respond_to_web_message(self, message):
        print(message)
        directive = message[0]
        print(directive)
        if directive == "C":  # A client is trying to log in, check if He exists in the Database
            params = message[1:].split("|")
            print("params: " + str(params))
            print("Checking client info")
            return self.check_client_info(params)
        else:
            return "message: " + message + ". Received"

    async def handler(self, websocket, path):
        async for request in websocket:
            print("request: " + request)
            response = await self.respond_to_web_message(request)
            await websocket.send(response)

    def __init__(self):
        start_server = websockets.serve(self.handler, '0.0.0.0', 5678)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()


def main():
    server = webserver()


if __name__ == '__main__':
    main()
