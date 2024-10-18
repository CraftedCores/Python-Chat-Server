# Import required Modules
import socket
import threading

HOST = '127.0.0.1'
PORT = 1234 # Can use any port from 0 - 65535
LISTENER_LIMIT = 5 # Limit of clients for server
active_clients = [] # list of all currently connected users

# Function to listen for any upcoming messages from a client
def listen_for_messages(client, username):
    
    while 1:
        message = client.recv(2048).decode('utf-8')
        if message != '':
            final_msg = username + '~' + message
            send_messages_to_all(final_msg)

        else:
            print(f"The message send from client {username} is empty ")


# Function to send message to a single client
def send_message_to_client(client, message):

    client.sendall(message.encode())


# Sends message to all clients connected to the server
def send_messages_to_all(message):

    for user in active_clients:
        send_message_to_client(user[1], message)



# Function to handle client
def client_handler(client):
    
    # Server will listen for client message that will
    # contain the username
    while 1:

        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
            prompt_message = "SERVER~" + f"{username} added to the chat"
            send_messages_to_all(prompt_message)
            break

        else:
            print("Client username is empty")

    threading.Thread(target=listen_for_messages, args=(client, username, )).start()


# Main Function
def main():
    # Creating the socket Class Object
    # AF_INET: we are going to use IPv4 Addresses
    # SOCK_STREAM: We are using TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Creating a try catch block
    try:
        # Provide the server with an address in the form of
        # host IP and port
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {PORT}")

    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")

    # Set server limit
    server.listen(LISTENER_LIMIT)

    # This while loop will keep listening to client connections
    while 1:

        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")

        # Starts a new thread everytime a new client is connected
        threading.Thread(target=client_handler, args=(client, )).start()




if __name__ == '__main__':
    main()

