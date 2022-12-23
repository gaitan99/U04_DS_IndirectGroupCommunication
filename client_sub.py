import socket
import sys
import select
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

broker_address = ('localhost', 10000)
port = 10001

successful_conection = False
server_address = ('localhost', port)

#Comprobamos que el puerto no esté y en caso de que lo esté
#probamos otros puertos hasta encontrar uno que no esté empleado
while not successful_conection:
    try:
        sock.bind(server_address)
        successful_conection = True
    except:
        print("Used port : ",port)
        port += 1
        print("Trying port : ",port)
        server_address = ('localhost', port)

#Preparamos el mensaje que le tenemos que enviar al broker
messageA = b'sub:id:%i'%port
messageB = b'sub:topic:game'


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    # Send data
    sock.bind(server_address)
    print('sending {!r}'.format(messageA))
    sent = sock.sendto(messageA, broker_address)
    print('sending {!r}'.format(messageB))
    sent = sock.sendto(messageB, broker_address)
finally:
    print('closing socket')
    sock.close()

# Bind the socket to the port
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', port)
sock.bind(server_address)
print('starting up on {} port {}'.format(*server_address))
while True:
    print('\nwaiting to receive message')
    rlist, _, _ = select.select([sock], [], []) 
    data, address = sock.recvfrom(1024)
    # Do stuff with data, fill this up with your code
    print('received {} bytes from {}'.format(len(data), address))
    print(data)

