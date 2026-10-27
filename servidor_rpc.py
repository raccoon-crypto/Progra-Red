from xmlrpc.server import SimpleXMLRPCServer


def saludar(apodo):
    print("Me llamaron con:", apodo)
    return "Hola, " + apodo + "!"


servidor = SimpleXMLRPCServer(("localhost", 5000))
servidor.register_function(saludar, "saludar")
print("Servidor RPC en el puerto 5000...")
servidor.serve_forever()
