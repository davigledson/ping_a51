from scapy.all import *
import time

import socket
import time

def send_file_via_udp(filename, host='127.0.0.1', port=9999):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    with open(filename, 'rb') as f:
        while True:
            data = f.read(1024)  # Lê o arquivo em blocos de 1024 bytes
            if not data:
                break
            sock.sendto(data, (host, port))
            time.sleep(0.01)  # Espera um pouco entre os pacotes

    # Envia sinalizador de fim
    sock.sendto(b'END', (host, port))
    print("Arquivo enviado com sucesso.")

    sock.close()

if __name__ == "__main__":
    send_file_via_udp("arquivo.txt")
