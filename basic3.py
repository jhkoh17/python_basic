# Unit 28
monday_temperatures = [9.1, 8.8, 7.5]

monday_temperatures.append(4)
print(monday_temperatures)

monday_temperatures.clear()
print(monday_temperatures)


monday_temperatures = [9.1, 8.8, 7.5]
print(monday_temperatures.index(8.8))

monday_temperatures.remove(9.1) # remove one item per code
monday_temperatures.remove(8.8)

print(monday_temperatures)

monday_temperatures = [9.1, 8.8, 7.5]
print(monday_temperatures[1])

monday_temperatures = [9.1, 8.8, 7.5, 6.6, 9.9]
print(monday_temperatures[1:])
print(monday_temperatures[2:4]) # the upper limit is not included.
print(monday_temperatures[-1])
print(monday_temperatures[:2])
print(monday_temperatures[-2:])
print(monday_temperatures[-1]) 
