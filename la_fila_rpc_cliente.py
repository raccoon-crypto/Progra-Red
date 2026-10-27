from xmlrpc.server import SimpleXMLRPCServer
import threading

# Variable global para el contador de turnos y el objeto de sincronización
turno_actual = 0
lock = threading.Lock()


def tomar_turno(apodo):
    global turno_actual
    # Protegemos la sección crítica con lock para evitar condiciones de carrera
    with lock:
        turno_actual += 1
        print(f"Turno asignado #{turno_actual} para el usuario: {apodo}")
        return turno_actual


def cuantos_van():
    with lock:
        return turno_actual


# Inicializar el servidor XML-RPC en localhost y puerto 5000
servidor = SimpleXMLRPCServer(("localhost", 5000))

# Registrar ambas funciones para que estén disponibles públicamente
servidor.register_function(tomar_turno, "tomar_turno")
servidor.register_function(cuantos_van, "cuantos_van")

print("Servidor de 'LA FILA' escuchando en el puerto 5000...")
servidor.serve_forever()
