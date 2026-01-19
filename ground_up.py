def calculate_force(m,a):
    return m*a 

m = float(input("mass= "))
a = float(input("acc= "))
F = calculate_force(m,a)
print(F)