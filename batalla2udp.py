import socket

FLOTA = {"A1", "A2", "B3"}  # Barcos secretos
PUERTO = 5050

# Crear socket UDP (SOCK_DGRAM)
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(("0.0.0.0", PUERTO))
print("Servidor UDP (Defensor) esperando ataques...")

try:
    while True:
        # En UDP no hay accept(), se recibe directamente con recvfrom indicando datos y la dirección del cliente
        data, addr = servidor.recvfrom(1024)
        ataque = data.decode("utf-8").strip().upper()
        print(f"Ataque recibido de {addr}: {ataque}")

        if ataque in FLOTA:
            respuesta = "TOCADO"
            FLOTA.remove(ataque)
        else:
            respuesta = "AGUA"

        # Enviar respuesta usando sendto hacia la dirección de origen del cliente
        servidor.sendto(respuesta.encode("utf-8"), addr)

        if not FLOTA:
            print("¡Toda la flota ha sido destruida!")
            break
finally:
    servidor.close()
