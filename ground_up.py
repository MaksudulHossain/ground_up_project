class PhysicsCalulator:
    def calculate_force(self, m,a):
        return m*a 
    
calculator = PhysicsCalulator() 

try:
    m = float(input("m=?"))
    a = float(input("a=?"))
    
    F = calculator.calculate_force(m,a)

    with open("results2.txt","a") as f:
        f.write(f"m={m}, a={a}, F={F}\n")
    
    print(f"F={F}")
    print("saved to results.txt")

except ValueError:
    print("Invalid input. Please enter numeric value.")
