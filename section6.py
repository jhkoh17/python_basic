# section 
def foo(values):
    if values > 7:
        return "Warm"
    else:
        return "Cold"
        
user_input = float(input("Enter temperature:")) # user's input is considered as string
print(foo(user_input))
