import socket
domain = input("Enter domain name: ")
ip=socket.gethostbyname(domain)
print("IP address of",domain,"is",ip)
