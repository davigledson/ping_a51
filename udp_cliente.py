import socket

def send_message(message):
    host = '127.0.0.1'  # Endereço do servidor
    port = 65432        # Porta do servidor

    # Cria o socket UDP e envia a mensagem
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.sendto(message.encode(), (host, port))
        print("Mensagem enviada ao servidor.")

# Envia uma mensagem de exemplo
send_message("Olá, Wireshark via UDP olaaaaa!")
