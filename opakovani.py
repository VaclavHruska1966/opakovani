import random

pole1 = []
pole2 = []

for i in range(random.randint(1,10)):
    pole1.append(random.randint(1, 10))
    pole1.sort()
print(pole1)

for j in range(random.randint(1,10)):
    pole2.append(random.randint(1, 10))
    pole2.sort()
print(pole2)



if pole1<pole2:
    print ("pole1 je větší než pole2")


elif pole1 > pole2:
    print("pole2 je větší než pole1")

