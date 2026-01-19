import logging 

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class PhysicsCalulator:
    def calculate_force(self, m,a):
        return m*a 
    
def main():
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
        logging.error("Invalid numeric input")
        print("Invalid input. Please enter numeric value.")


if __name__ == '__main__':
    main()