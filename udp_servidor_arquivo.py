import socket
import subprocess
# baixar a versao gpg4win-4.3.1
# baixar o socket

# 1 passo - rodar o arquivo udp_servidor_arquivo.python
# 2 passo - colocar a chave publica no arquivo cliente
# 3 passo - rodar o arquivo udp_cliente_arquivo.python



def start_udp_server(host='127.0.0.1', port=9999):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print(f'Servidor UDP em execução em {host}:{port}')

    with open('arquivo.txt.gpg', 'wb') as f:
        while True:
            data, addr = sock.recvfrom(1024)  # Buffer de 1024 bytes
            if data == b'END':  # Sinaliza o fim da transferência
                print("Transferência de arquivo concluída.")
                break
            f.write(data)
            print(f'Pacote recebido de {addr}')

    sock.close() 

    try:
        subprocess.run(['gpg', '--output', 'arquivo_recebido.txt', '--decrypt', 'arquivo.txt.gpg'], check=True)
        print("Arquivo descriptografado com sucesso como 'arquivo_recebido.txt'.")
    except subprocess.CalledProcessError:
        print("Erro ao descriptografar o arquivo.")

if __name__ == "__main__":
    start_udp_server()
