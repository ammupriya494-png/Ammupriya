import socket
hostname=socket.gethostname()
ip_address=socket.gethostbyname(hostname)
print("Your Computer Name:",hostname)
print("Your IP Address:",ip_address)
