
from Challengemain import User, Intern, Mentor, Admin, HR

intern = Intern("Badar", "Halley")
mentor = Mentor("Chahat", "Data Science")
admin = Admin(User("Danial"), "IT")
hr = HR(User("Elia"), "Punjab")
print(intern.login())
print(intern.log_task("Setup development environment"))

print(mentor.login())
print(mentor.teach("Neural Networks"))

print(admin.audit("Security"))

print(hr.hire("Eva"))
