class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}."

class Intern(User):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def work(self):
        return f"{self.name} is interning from {self.school}."

class Mentor(User):
    def __init__(self, name, expertise):
        super().__init__(name)
        self.expertise = expertise

    def teach(self):
        return f"{self.name} is mentoring with expertise in {self.expertise}."

user = User("Muhammad")
intern  = Intern("Haider", "Softsinc")
mentor = Mentor("Abbas", "Machine Learning")

print(user.greet())        
print(intern.work())       
print(mentor.teach())    