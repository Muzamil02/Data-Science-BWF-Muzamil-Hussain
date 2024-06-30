class User:
    def __init__(self, first_name, last_name, age, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Profile:")
        print(f"  First Name: {self.first_name}")
        print(f"  Last Name: {self.last_name}")
        print(f"  Age: {self.age}")
        print(f"  Email: {self.email}")
        print(f"  Username: {self.username}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, welcome back!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Muzamil", "Hussain", 22, "my123@gmail.com", "muxu_0")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"Login attempts: {user1.login_attempts}")
user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")

user2 = User("Ahmed", "Ali", 28, "ahmed1Agmail.com", "ahmed_1")
user2.increment_login_attempts()
user2.increment_login_attempts()

print(f"Login attempts: {user2.login_attempts}")
user2.reset_login_attempts()
print(f"Login attempts after reset: {user2.login_attempts}")

user3 = User("Husnain", "Ahmed", 21, "hasnain@gmail.com", "hasnin_5")
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()

print(f"Login attempts: {user3.login_attempts}")
user3.reset_login_attempts()
print(f"Login attempts after reset: {user3.login_attempts}")