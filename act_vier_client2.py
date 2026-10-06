import socket
import sys

# Cambiar por la IP del servidor (quien ejecuta el ejercicio 6)
SERVER_IP = "192.168.1.1"
TCP_PORT = 5000
UDP_PORT = 5001


def pedir_turno():
    """Pide un turno por TCP."""
    with socket.create_connection((SERVER_IP, TCP_PORT), timeout=5) as s:
        s.sendall(b"TURNO\n")
        respuesta = s.recv(4096).decode("utf-8").strip()
        print("Servidor:", respuesta)


def consultar_total():
    """Consulta cuántos turnos se han repartido por UDP."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)
        s.sendto(b"CUANTOS\n", (SERVER_IP, UDP_PORT))
        respuesta, _ = s.recvfrom(4096)
        print("Servidor:", respuesta.decode("utf-8").strip())


if __name__ == "__main__":
    if len(sys.argv) > 1:
        opcion = sys.argv[1].lower()
    else:
        opcion = input("¿Qué quieres hacer? (turno / cuantos): ").strip().lower()

    if opcion == "turno":
        pedir_turno()
    elif opcion == "cuantos":
        consultar_total()
    else:
        print("Opciones: 'turno' o 'cuantos'")
