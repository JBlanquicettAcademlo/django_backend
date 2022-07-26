import socket

s = socket.socket()

print("Socket created")

port = 9000

s.bind(('', port))
s.listen(5)

response = {'status': 'success', 'message': 'Server is running'}

while True:

    c, addr = s.accept()
    print("Got connection from", addr)

    c.send(f'{response}'.encode())
    c.close()
    print("Closed connection")
    break
