# main_script.py
from Task3 import write_to_file
import datetime

def log_action(action: str, user: str):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {user}: {action}\n"
    write_to_file("activity.log", log_entry)



class User:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        self.name = name

    def greet(self):
        log_action("Greeted", self.name)
        return f"Hello, I'm {self.name}."

    def login(self):
        log_action("Logged in", self.name)
        return f"{self.name} has logged in."

    def send_message(self, message):
        log_action(f"Sent message: {message}", self.name)
        return f"{self.name} says: {message}"

    def perform_role(self):
        return "I am a general user."

    def __str__(self):
        return f"User(Name: {self.name})"


class Intern(User):
    def __init__(self, name, school):
        super().__init__(name)
        if not isinstance(school, str) or not school.strip():
            raise ValueError("School must be a non-empty string.")
        self.school = school

    def work(self):
        log_action("Performed internship task", self.name)
        return f"{self.name} is interning from {self.school}."

    def perform_role(self):
        return self.work()

    def __str__(self):
        return f"Intern(Name: {self.name}, School: {self.school})"


class Mentor(User):
    def __init__(self, name, expertise):
        super().__init__(name)
        if not isinstance(expertise, str) or not expertise.strip():
            raise ValueError("Expertise must be a non-empty string.")
        self.expertise = expertise

    def teach(self):
        log_action("Conducted mentoring session", self.name)
        return f"{self.name} is mentoring with expertise in {self.expertise}."

    def perform_role(self):
        return self.teach()

    def __str__(self):
        return f"Mentor(Name: {self.name}, Expertise: {self.expertise})"


class Admin:
    def __init__(self, user: User, department: str):
        if not isinstance(department, str) or not department.strip():
            raise ValueError("Department must be a non-empty string.")
        self.user = user
        self.department = department

    def perform_role(self):
        log_action(f"Administered {self.department} department", self.user.name)
        return f"{self.user.name} is an admin in the {self.department} department."

    def __str__(self):
        return f"Admin(User: {self.user.name}, Department: {self.department})"


class HR:
    def __init__(self, user: User, region: str):
        if not isinstance(region, str) or not region.strip():
            raise ValueError("Region must be a non-empty string.")
        self.user = user
        self.region = region

    def perform_role(self):
        log_action(f"Managed HR for {self.region}", self.user.name)
        return f"{self.user.name} is an HR representative for the {self.region} region."

    def __str__(self):
        return f"HR(User: {self.user.name}, Region: {self.region})"

user = User("Ahmad")
intern = Intern("Badar", "Halley")
mentor = Mentor("Chahat", "Data Science")
admin = Admin(User("Danial"), "IT")
hr = HR(User("Elia"), "Punjab")
print("\n--- Object Info ---")
print(user)
print(intern)
print(mentor)
print(admin)
print(hr)
print("\n--- Actions ---")
print(user.login())
print(user.send_message("Hi there!"))
print(intern.login())
print(intern.work())
print(mentor.login())
print(mentor.teach())
print(admin.perform_role())
print(hr.perform_role())
