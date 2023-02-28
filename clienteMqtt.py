import asyncio, ssl, certifi
from asyncio_mqtt import Client, ProtocolVersion
from environs import Env

env = Env()
env.read_env() #lee el archivo con las variables. por defecto .env

async def main():
    tls_context = ssl.create_default_context()
    tls_context.load_verify_locations(certifi.where())

    async with Client(
        env("SERVIDOR"),
        protocol=ProtocolVersion.V31,
        port=8883,
        tls_context=tls_context,
    ) as client:
        async with client.messages() as messages:
            await client.subscribe("#")
            async for message in messages:
                print(str(message.topic) + ": " + message.payload.decode("utf-8"))

if __name__ == "__main__":
    asyncio.run(main())
