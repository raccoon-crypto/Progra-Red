import socket

HOST = "148.226.51.170"
PORT = 34567

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Cliente inicia la conexión TCP")
print("1. Cliente -> Servidor: SYN")
print("2. Servidor -> Cliente: SYN-ACK")
print("3. Cliente -> Servidor: ACK")
print("✅ Handshake completado")

client.sendall(b"Hola servidor, quiero conectarme")

respuesta = client.recv(1024).decode("utf-8")
print(f"Respuesta del servidor: {respuesta}")

client.close()
