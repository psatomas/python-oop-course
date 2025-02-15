class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age
    def presentation(self):
        print(f"your name is {self.username} and you are {self.age}")


user1 = User("tomás", 32)
user1.presentation()