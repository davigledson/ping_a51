import socket

def start_udp_server(host='127.0.0.1', port=9999):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print(f'Servidor UDP em execução em {host}:{port}')

    with open('arquivo.txt', 'wb') as f:
        while True:
            data, addr = sock.recvfrom(1024)  # Buffer de 1024 bytes
            if data == b'END':  # Sinaliza o fim da transferência
                print("Transferência de arquivo concluída.")
                break
            f.write(data)
            print(f'Pacote recebido de {addr}: {data}')

    sock.close()

if __name__ == "__main__":
    start_udp_server()
