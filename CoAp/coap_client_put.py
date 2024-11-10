import logging
import asyncio
from aiocoap import *

logging.basicConfig(level=logging.INFO)

async def main():
    context = await Context.create_client_context()
    #await asyncio.sleep(2)

    #payload = b"Perform a single PUT request to localhost on the default port.\n"
    payload = "我是 CoAP Client Put，到此一遊！\n".encode("utf-8")

    request = Message(code=PUT, payload=payload, uri="coap://localhost/hello/goomo")

    response = await context.request(request).response

    #print('Result: %s\n%r'%(response.code, response.payload))
    print('Result: %s\n%s' % (response.code, response.payload.decode("utf-8")))

if __name__ == "__main__":
    asyncio.run(main())