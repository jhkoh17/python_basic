# Section 5
# Unit 37
def mean0(mylist): # parameters (i.e., inputs)
    the_mean = sum(mylist)/len(mylist)
    return the_mean # if "return" is missing, "None" will be created.


def mean(value): # parameters (i.e., inputs)
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value)/len(value)
    
    return the_mean # if "return" is missing, "None" will be created.

student_grades = {"Smith": 9.9, "John":8.8, "Sam": 3.5}
print(mean(student_grades))

# in 
def foo(x, array):
    if x in array:
        return True
    else: 
        return False

print(foo(1, [1,3,5]))


# isinstantance 

def mean2(value): # parameters (i.e., inputs)
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value)/len(value)
    
    return the_mean # if "return" is missing, "None" will be created.

student_grades = {"Smith": 9.9, "John":8.8, "Sam": 3.5}
print(mean2(student_grades))

# Coding Activity
def foo(values):
    if len(values) >= 8:
        return True # use "return" than "print"
    else:
        return False

foo("mypass")

# Unit 44
x = 3
y = 1
if x>y:
    print("x is greater than y.")
elif x ==y:
    print("x is equal to y.")
else:
    print("x is smaller than y.")

