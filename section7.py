# Unit 51: For Loops
monday_temp = [9.9, 6.1, 8.9]

for temperature in monday_temp:
    print(round(temperature))
    print("done")

for letter in "Hello":
    print(letter.upper())

# Unit 54: iteration over a dictionary
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for pair in phone_numbers.items():
    print("Item:", pair)
for pair in phone_numbers.keys():
    print("Keys: ", pair)
for key, value in phone_numbers.items():
    print("{} has a phone number {}".format(key, value))


# Unit 56: While loop
a = 3 
while 0 <a<10:
    print(a)
    a = a + 1

# Unit 57: 
username = ''

# while username !="pypy": # countinue until the statement is false
#     username = input("Enter username: ")

while True:
    username = input("Enter username: ")
    if username == "pypy":
        break
    else:
        continue