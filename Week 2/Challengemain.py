
from Challengerolelogger import log_role_action

class User:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        self.name = name

    def login(self):
        log_role_action("user", self.name, "Logged in")
        return f"{self.name} has logged in."

    def send_message(self, message):
        log_role_action("user", self.name, f"Sent message: {message}")
        return f"{self.name} says: {message}"

    def __str__(self):
        return f"User(Name: {self.name})"


class Intern(User):
    def __init__(self, name, school):
        super().__init__(name)
        if not isinstance(school, str) or not school.strip():
            raise ValueError("School must be a non-empty string.")
        self.school = school

    def log_task(self, task):
        log_role_action("intern", self.name, f"Completed task: {task}")
        return f"{self.name} completed task: {task}"

    def __str__(self):
        return f"Intern(Name: {self.name}, School: {self.school})"


class Mentor(User):
    def __init__(self, name, expertise):
        super().__init__(name)
        if not isinstance(expertise, str) or not expertise.strip():
            raise ValueError("Expertise must be a non-empty string.")
        self.expertise = expertise

    def teach(self, topic):
        log_role_action("mentor", self.name, f"Taught topic: {topic}")
        return f"{self.name} taught topic: {topic}"

    def __str__(self):
        return f"Mentor(Name: {self.name}, Expertise: {self.expertise})"


class Admin:
    def __init__(self, user: User, department: str):
        if not isinstance(department, str) or not department.strip():
            raise ValueError("Department must be a non-empty string.")
        self.user = user
        self.department = department

    def audit(self, area):
        log_role_action("admin", self.user.name, f"Audited {area}")
        return f"{self.user.name} audited {area} in {self.department} department."

    def __str__(self):
        return f"Admin(User: {self.user.name}, Department: {self.department})"


class HR:
    def __init__(self, user: User, region: str):
        if not isinstance(region, str) or not region.strip():
            raise ValueError("Region must be a non-empty string.")
        self.user = user
        self.region = region

    def hire(self, candidate):
        log_role_action("hr", self.user.name, f"Hired {candidate}")
        return f"{self.user.name} hired {candidate} in the {self.region} region."

    def __str__(self):
        return f"HR(User: {self.user.name}, Region: {self.region})"
