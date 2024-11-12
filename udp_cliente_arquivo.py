import socket
import time
import subprocess

def encrypt_file_with_public_key(filename, recipient):
    """Criptografa o arquivo usando GPG e a chave pública do destinatário."""
    try:
        subprocess.run(['gpg', '--output', f"{filename}.gpg", '--encrypt', '--recipient', recipient, filename], check=True)
        print(f"Arquivo '{filename}' criptografado com sucesso como '{filename}.gpg'.")
    except subprocess.CalledProcessError:
        print("Erro ao criptografar o arquivo.")
        return False
    return True

def send_file_via_udp(filename, host='127.0.0.1', port=9999):
    """Envia o arquivo criptografado via UDP."""
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
    original_filename = "arquivo.txt"
    encrypted_filename = f"{original_filename}.gpg"
    recipient = "E7E7F0DCE8E6AAD877AFE08CC426E2A89F6A8474"  
    
    if encrypt_file_with_public_key(original_filename, recipient):
        
        send_file_via_udp(encrypted_filename)
