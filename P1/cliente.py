import socket
from cryptography.fernet import Fernet

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'SEND archivo.txt')
    data = s.recv(1024)
    if data == b'OK':
        file_data = s.recv(4096)
        print('Ingresa la llave: ', end=" ")
        key = input()
        if len(key) == 44:
            cipher_suite = Fernet(key.encode())
            # Desencripta el mensaje si la llave es correcta
            plain_text = cipher_suite.decrypt(file_data)
            with open('archivo_descargado.txt', 'wb') as f:
                f.write(plain_text)
        else:
            print("Error, llave incorrecta")
    else:
        print('Error al recibir el archivo')