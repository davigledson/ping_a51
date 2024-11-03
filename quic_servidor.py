import asyncio
from aioquic.asyncio import QuicConnectionProtocol, serve
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import StreamDataReceived

class EchoQuicProtocol(QuicConnectionProtocol):
    async def quic_event_received(self, event):
        if isinstance(event, StreamDataReceived):
            # Exibe uma mensagem indicando que o servidor recebeu dados
            print(f"Servidor: Mensagem recebida - {event.data.decode()}")
            # Envia uma resposta para o cliente
            self._quic.send_stream_data(event.stream_id, event.data + b" - Recebido pelo servidor QUIC")
            print("Servidor: Resposta enviada ao cliente.")

async def main():
    configuration = QuicConfiguration(is_client=False)
    await serve("0.0.0.0", 4433, configuration=configuration, create_protocol=EchoQuicProtocol)
    print("Servidor QUIC em execução e aguardando conexões...")

asyncio.run(main())
