import asyncio
from aioquic.asyncio import connect
from aioquic.quic.configuration import QuicConfiguration
# ambiente_virtual\Scripts\activate (ativa ambiente virtual)
async def run_client():
    configuration = QuicConfiguration(is_client=True)
    configuration.verify_mode = False  # Ignora a validação de certificados

    async with connect("localhost", 4433, configuration=configuration) as protocol:
        # Obtém o próximo stream disponível e envia dados
        stream_id = protocol._quic.get_next_available_stream_id()
        message = b"Ola, servidor QUIC"
        protocol._quic.send_stream_data(stream_id, message)

        print("Cliente: Mensagem enviada ao servidor.")

        await protocol._quic.wait_closed()
        print("Cliente: Conexão encerrada com sucesso.")


asyncio.run(run_client())
