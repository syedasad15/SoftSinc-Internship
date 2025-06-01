class User:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}."

    def __str__(self):
        return f"User(Name: {self.name})"


class Intern(User):
    def __init__(self, name, school):
        super().__init__(name)
        if not isinstance(school, str) or not school.strip():
            raise ValueError("School must be a non-empty string.")
        self.school = school

    def work(self):
        return f"{self.name} is interning from {self.school}."

    def __str__(self):
        return f"Intern(Name: {self.name}, School: {self.school})"


class Mentor(User):
    def __init__(self, name, expertise):
        super().__init__(name)
        if not isinstance(expertise, str) or not expertise.strip():
            raise ValueError("Expertise must be a non-empty string.")
        self.expertise = expertise

    def teach(self):
        return f"{self.name} is mentoring with expertise in {self.expertise}."

    def __str__(self):
        return f"Mentor(Name: {self.name}, Expertise: {self.expertise})"

def create_user():
    name = input("Enter user name: ")
    return User(name)

def create_intern():
    name = input("Enter intern's name: ")
    school = input("Enter intern's school: ")
    return Intern(name, school)

def create_mentor():
    name = input("Enter mentor's name: ")
    expertise = input("Enter mentor's area of expertise: ")
    return Mentor(name, expertise)

user = create_user()
intern = create_intern()
mentor = create_mentor()
print("\nObjects created:")
print(user)
print(intern)
print(mentor)
print("\nBehavior:")
print(user.greet())
print(intern.work())
print(mentor.teach())    