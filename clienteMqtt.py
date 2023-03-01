import asyncio, ssl, certifi
from asyncio_mqtt import Client, ProtocolVersion
from environs import Env

env = Env()
env.read_env() #lee el archivo con las variables. por defecto .env

async def main():
    tls_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    tls_context.verify_mode = ssl.CERT_REQUIRED
    tls_context.check_hostname = True
    tls_context.load_default_certs()

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
