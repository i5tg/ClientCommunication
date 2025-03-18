import socket
SERVER_ADDRESS = input("Enter server IP address: ")
try:
  SERVER_PORT = int(input("Enter server port number: "))
  if not (1024 <= SERVER_PORT <= 65535):
    raise ValueError("Invalid port number. Please enter a value between 1024 and 65535.")
except ValueError as error:
  print("Error:", error)
  exit()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
  print("Connected to server at", SERVER_ADDRESS, ":", SERVER_PORT)

  message = "[+] Connection Established. "
  client_socket.sendall(message.encode())
  received_data = client_socket.recv(1024).decode()
  if received_data:
    print("Received from server:", received_data)
  else:
    print("Server did not send any data.")
  while True:
    message = input("Send Message to server: ")
    if message == "quit":
      break
    client_socket.sendall(message.encode())

    try:
      received_data = client_socket.recv(1024).decode()
    except (ConnectionError, ConnectionAbortedError) as error:
      print("Connection error:", error)
      break  

    if received_data:
      print("Received from server:", received_data)
    else:
      print("Server did not send any data (or connection closed).")

except (ConnectionRefusedError, OSError) as error:
  print("Connection failed:", error)

finally:
  client_socket.close()
  print("Connection closed.")

#Made by i5tg on discord
