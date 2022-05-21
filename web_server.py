"""
A Server meant to deal with web clients. This is different from the main server because it requires utilisation of
websocket.
Additionally, I used asyncio for the web server because I could not get it to work without async
Async Explanation: https://www.aeracode.org/2018/02/19/python-async-simplified/
"""
import websockets
import asyncio

class webserver:

    async def respond_to_web_message(self, message):
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
