class Message:
    def __init__(self, sender, receiver, content):
        if not content.strip():
            raise ValueError("Message content cannot be empty.")
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def __str__(self):
        return f"{self.sender.name} --> {self.receiver.name}: {self.content}"

class User:
    def __init__(self, name):
        if not name.strip():
            raise ValueError("Name must be a non-empty string.")
        self.name = name
        self.inbox = []

    def send_message(self, receiver, content, chat_app):
        message = Message(self, receiver, content)
        chat_app.store_message(message)
        receiver.receive_message(message)

    def receive_message(self, message):
        self.inbox.append(message)

    def view_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        if not self.inbox:
            print("No messages.")
        for msg in self.inbox:
            print(msg)


class Manager(User):
    def __init__(self, name):
        super().__init__(name)

    def view_all_messages(self, chat_app):
        print(f"\nManager {self.name} - All Messages:")
        for msg in chat_app.messages:
            print(msg)


class ChatApp:
    def __init__(self):
        self.messages = []

    def store_message(self, message):
        self.messages.append(message)

app = ChatApp()
alice = User("Alice")
bob = User("Bob")
manager = Manager("Carol")

alice.send_message(bob, "Hey Bob!", app)
bob.send_message(alice, "Hi Alice!", app)
bob.send_message(manager, "Hi Manager!", app)

alice.view_inbox()
bob.view_inbox()
manager.view_inbox()
manager.view_all_messages(app)
