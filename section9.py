# List Comphresion
temps = [221, 234, -9999, 340, 230]

new_temp = [temp/10 for temp in temps]

print(new_temp)

new_temp1 = [temp/10 for temp in temps if temp !=-9999]

print(new_temp1)