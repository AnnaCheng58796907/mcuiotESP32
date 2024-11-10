import datetime
import logging
import asyncio
import aiocoap.resource as resource
import aiocoap


# Example resource which supports the GET and PUT methods.
class Hello_Resource(resource.Resource):
    def __init__(self):
        super().__init__()
        #self.set_content(b"This is the resource's default content.\n")
        self.set_content("我是 CoAP Server 預設的訊息！\n".encode("utf-8"))

    def set_content(self, content):
        self.content = content

    async def render_get(self, request):
        return aiocoap.Message(payload=self.content)

    async def render_put(self, request):
        #print('PUT payload: %s' % request.payload)
        print('PUT payload: %s' % request.payload.decode("utf-8"))
        self.set_content(request.payload)
        return aiocoap.Message(code=aiocoap.CHANGED, payload=self.content)


async def main():
    # logging setup
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("coap-server").setLevel(logging.DEBUG)

    # Resource tree creation
    root = resource.Site()
    root.add_resource(['hello', 'goomo'], Hello_Resource())

    await aiocoap.Context.create_server_context(site=root, bind=('localhost', 5683))
    
    # Run forever
    await asyncio.get_running_loop().create_future()


if __name__ == "__main__":
    asyncio.run(main())