def calculate_force(m,a):
    return m*a 
try:
    m = float(input("mass= "))
    a = float(input("acc= "))
    F = calculate_force(m,a)
    print(F)
except ValueError:
    print("Invalidd input. Please enter numeric val.")