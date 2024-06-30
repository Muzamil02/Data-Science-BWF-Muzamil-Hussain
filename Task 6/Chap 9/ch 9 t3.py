class User:
    def __init__(self, first_name, last_name, age, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.username = username

    def describe_user(self):
        print(f"User Profile:")
        print(f"  First Name: {self.first_name}")
        print(f"  Last Name: {self.last_name}")
        print(f"  Age: {self.age}")
        print(f"  Email: {self.email}")
        print(f"  Username: {self.username}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, welcome back!")

user1 = User("Muzamil", "Hussain", 22, "my123@gmail.com", "muxu_0")         #User class instances
user2 = User("Ahmed", "Ali", 28, "ahmed1Agmail.com", "ahmed_1")
user3 = User("Husnain", "Ahmed", 21, "hasnain@gmail.com", "hasnin_5")


user1.describe_user()           #calling methods
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
