import socket

# Define the DNS server's IP address and port
DNS_SERVER_IP = '10.10.10.1'
DNS_SERVER_PORT = 12345

# Define the domain name to look up
domain = 'google.com'

# Create a UDP socket and send a DNS query packet to the server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(domain.encode(), (DNS_SERVER_IP, DNS_SERVER_PORT))

# Receive the DNS response packet from the server and decode it
data, addr = sock.recvfrom(1024)
ip_address = data.decode().strip()

print('{} resolves to {}'.format(domain, ip_address))
