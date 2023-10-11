import socket
from cryptography.fernet import Fernet

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    print('Servidor escuchando...')
    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        data = conn.recv(1024)
        comando, nombre_archivo = data.decode('utf-8').split(' ')
        if comando == 'SEND':
            try:
                with open(nombre_archivo, 'rb') as f:
                    file_data = f.read()
                conn.sendall(b'OK')
                # Genera una clave de cifrado aleatoria
                key = Fernet.generate_key()
                cipher_suite = Fernet(key)
                print(key.decode())
                # Encripta el mensaje
                cipher_text = cipher_suite.encrypt(file_data)
                conn.sendall(cipher_text)
            except:
                conn.sendall(b'ERROR')
