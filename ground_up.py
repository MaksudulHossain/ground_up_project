def calculate_force(m,a):
    return m*a 

try:
    m = float(input("mass= "))
    a = float(input("acc= "))
    F = calculate_force(m,a)
    # print(F)

    with open("results.txt", "a") as f:
        f.write(f"m={m}, a={a}, F={F}\n")

    print(f"Force: {F}")
    print("Saved to resuls.txt")
    
except ValueError:
    print("Invalidd input. Please enter numeric val.")