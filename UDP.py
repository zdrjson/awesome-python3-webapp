s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1'), 9999)
print('Bind UDP on 999...')

while True:
	data, addr = s.recvfrom(2014)
	print('Received from %s:%s.' % addr)
	s.sendto(b'Hello, %s!' % data, addr)
	