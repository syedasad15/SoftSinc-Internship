class User:
    def __init__(self, name):
        self.name = name

class Intern(User):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

class Mentor(User):
    def __init__(self, name, expertise):
        super().__init__(name)
        self.expertise = expertise

user = User("Muhammad")
intern  = Intern("Haider", "Softsinc")
mentor = Mentor("Abbas", "Machine Learning")
print(user.name)        
print(intern.school)
print(intern.name) 
print(mentor.expertise)
print(mentor.name)        
