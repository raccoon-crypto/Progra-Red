import socket

FLOTA = {"A1", "A2", "B3"}  # barcos secretos (5x5: A-E)
PUERTO = 5050  # port (puerto) acordado

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("0.0.0.0", PUERTO))  # bind (asociar)
servidor.listen(1)  # listen (escuchar)
print("Esperando al atacante...")

conn, addr = servidor.accept()
print(f"Conectado con el atacante: {addr}")

try:
    while True:
        # Recibir ataque (request)
        data = conn.recv(1024).decode("utf-8")
        if not data:
            break

        ataque = data.strip().upper()
        print(f"Atacaron a: {ataque}")

        # Lógica de la batalla naval
        if ataque in FLOTA:
            respuesta = "TOCADO"
            FLOTA.remove(ataque)  # Eliminar para evitar repetir el mismo barco
        else:
            respuesta = "AGUA"

        # Enviar respuesta codificada (response)
        conn.send(respuesta.encode("utf-8"))

        if not FLOTA:
            print("¡Toda la flota ha sido destruida!")
            break
finally:
    conn.close()
    servidor.close()
