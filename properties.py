class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print("Email acessed")
        return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email


user1 = User("danthman", "dan@gmail.com", "123")
user1.email = "this is not an email"
print(user1.email)