# name = input("Enter your name: ")
# sur_name = input("Enter your surname: ")
# when = input("What is today?")
# message = "Hello %s %s" % (name, sur_name) 
# message = f"Hello {name} {sur_name}. What's up {when} ?"
# print(message)
def foo(values):
    message = f"Hi {values}"
    return message

print(foo("Jung"))

# # Uppercase: use string.title()
def foo1(name):
    return "Hi %s" % name.title()
print(foo1("jung"))