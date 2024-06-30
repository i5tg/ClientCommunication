import socket

def get_valid_port():
  while True:
    try:
      port = int(input("Please enter a port number: "))
      if 1024 <= port <= 65535:
        return port
      else:
        print("Invalid port number. Please try again.")
    except ValueError:
      print("Invalid input. Please enter a number.")


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Initializing.. | [+]")
well_known_port = get_valid_port()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', well_known_port))
sock.listen(5)

try:
  while True:
    newSocket, address = sock.accept()
    print ("Connected from", address)
    try:
      while True:
        receivedData = newSocket.recv(1024)
        if not receivedData:  # Handle no data received
            break
        print("Received:", receivedData.decode())
        newSocket.sendall(receivedData)  # Echo back received data
    except (ConnectionError, ConnectionAbortedError):
      print("Connection with", address, " terminated unexpectedly")
    finally:
      newSocket.close()
      print ("Disconnected from ", address)
finally:
  sock.close()
  print("Server shutting down.")

#made by metamethod3 on discord
#LongYears9 on Github.