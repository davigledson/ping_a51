import socket

def start_server():
    host = '127.0.0.1'  # Endereço IP local
    port = 65432        # Porta para escutar

    # Cria o socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Servidor UDP escutando em {host}:{port}")

        while True:
            data, addr = server_socket.recvfrom(1024)  # Recebe dados
            print(f"Mensagem recebida de {addr}: {data.decode()}")  # Exibe no terminal

start_server()
