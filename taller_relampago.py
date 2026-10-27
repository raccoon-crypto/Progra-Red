# Ejercicio 1
# mi_ip = "192.168.1.50"
# mi_puerto = 5000

# print(f"{mi_ip}:{mi_puerto}")

# ejercicio 2
# def es_puerto_valido(puerto):
#    return 0 <= puerto <= 65535


# print(es_puerto_valido(5000))
# print(es_puerto_valido(70000))


def construir_mensaje(ana, luis, texto):
    return f"De:{ana}\n Para: {luis}\n Mensaje: {texto}"


print(construir_mensaje("ana", "luis", "Nos vemos a las 3"))
