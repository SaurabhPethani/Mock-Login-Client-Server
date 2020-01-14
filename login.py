import socket

client = socket.socket()

client.connect(('localhost', 3888))

print("You Connected successfully!")

uname = input("Please enter username: ")
password = input("Please enter password: ")

client.send(uname.encode('utf-8'))
client.send(password.encode('utf-8'))

validate = client.recv(1024).decode('utf-8')

if validate == 'valid':
    print("1. Frequency\n2. Dictionary\n3. Math Operation\n")
    choice = int(input("Please Enter your Choice: "))
    client.send(str(choice).encode('utf-8'))

    if choice == 1:
        freq = input('Please Enter the number : ')
        client.send(freq.encode('utf-8'))
        result = client.recv(1024).decode('utf-8')
        print(result)
        
    elif choice == 2:
        print("Please Enter the word: ")
        word = input().encode('utf-8')
        client.send(word)
        result = client.recv(1024).decode('utf-8')
        print(result)
    elif choice == 3:
        d = {1:'add', 2:'div', 3:'mul', 4:'sub'}
        print("Please enter 1st number: ")
        num1 = int(input())
        print("please enter 2nd number: ")
        num2 = int(input())
        print("\nEnter the choice: \n1.Addition\n2.Division\n3.Multiplication\n4.Subtraction\n")
        operation = int(input())
        client.send(str(num1).encode('utf-8'))
        client.send(str(num2).encode('utf-8'))
        client.send(d[operation].encode('utf-8'))
        result = client.recv(1024).decode('utf-8')
        print(result)
else:
    print("Invalid User")    