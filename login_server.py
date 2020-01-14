import socket

ss = socket.socket()

ss.bind(('localhost', 3888))

ss.listen(3)

client,addr = ss.accept()
print(type(client))
print("Client connected!")

uname = client.recv(1024).decode('utf-8')
password = client.recv(1024).decode('utf-8')

class User:
	def __init__(self):	
		self.processFile()	

	def checkCredential(self, uname, password):
		if uname in self.uname_list:
			if password in self.pass_list:
				print("Authentic")
				client.send("valid".encode('utf-8'))

				choice = int(client.recv(1024).decode('utf-8'))
				if choice == 1:
					freq = int(client.recv(1024).decode('utf-8'))
					test = open('freq.txt', 'r')
					content = test.read().split()
					content = map(int, content)

					count = 0
					for val in content:
						if val == freq:
							count += 1

					client.send(str(count).encode('utf-8'))
				elif choice == 2:
					word = client.recv(1024).decode('utf-8')
					test = open('dictionary.txt', 'r')
					dictionary = {}
					for line in test.readlines():
							a = line.split(':')
							dictionary[a[0]] = a[1]
					if word in dictionary.keys():
							print("Word found with meaning ", dictionary[word])
							client.send(dictionary[word].encode('utf-8'))

				elif choice == 3:
					num1 = client.recv(1024).decode('utf-8')
					num2 = client.recv(1024).decode('utf-8')
					operation = client.recv(1024).decode('utf-8')
					res = None
					if operation == 'add':
						res = eval(num1)  + eval(num2)
						res = "Addition is " + str(res)
					elif operation == 'mul':
						res = eval(num1) * eval(num2)
						res = "Multiplication is "+ str(res)
					elif operation == 'div':
						res = eval(num1) / eval(num2)
						res = "Division is "+ str(res)
					elif operation == 'sub':
						res = eval(num1) - eval(num2)
						res = "Subtraction is "+ str(res)
					client.send(res.encode('utf-8'))
			else:
				print("Password Invalid")
				client.send("invalid".encode('utf-8'))
				
		else:
    			print("User Invalid")     
    			client.send("invalid".encode('utf-8'))
	
	def processFile(self):				
		file = open('login_creds.txt', 'r')

		self.uname_list = []
		self.pass_list = []
		for line in file.readlines():
			val = line.split()
			if val[0] == 'username':
				self.uname_list.append(val[1])
			elif val[0] == 'password':
				self.pass_list.append(val[1])
user = User()
user.checkCredential(uname, password)