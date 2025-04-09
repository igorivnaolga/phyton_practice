from queue import Queue
import random

class Client:
    def __init__(self, name):
        self.name = name
        self.operations = random.randint(1, 5)  # Random number of operations

class Bank:
    def __init__(self):
        self.clients = Queue()

    def new_client(self, client):
        self.clients.put(client)

    def serve_clients(self):
        while not self.clients.empty():
            current_client = self.clients.get()
            print(f"Serving client {current_client.name} with {current_client.operations} operations")
            # Here you can simulate processing time or add more logic

# Create the bank
bank = Bank()

# Add clients
for i in range(5):
    bank.new_client(Client(f"Client-{i}"))

# Serve clients
bank.serve_clients()

