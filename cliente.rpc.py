import xmlrpc.client

servidor = xmlrpc.client.ServerProxy("http://localhost:5000")
respuesta = servidor.saludar("ana")
print(respuesta)
