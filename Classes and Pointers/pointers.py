n1 = 11
n2 = n1

print("Before n2 value is updated")
print("n1 = ",n1)
print("n2 = ",n2)

print("\nn1 points to : ",id(n1))
print("n2 points to : ", id(n2))

n2 = 22
print("After n2 value is updated")
print("n1 = ",n1)
print("n2 = ",n2)

print("\nn1 points to : ",id(n1))
print("n2 points to : ", id(n2))
