import logging 

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s -%(message)s"
)

class InvalidPhysicsValue(Exception):
    """Custom Exception for invalid physics input."""
    pass 

class PhysicsCalculator:
    def calculate_force(self, m, a):
        if m<0:
            raise InvalidPhysicsValue("Mass cannot be negative")
        if a < 0:
            raise InvalidPhysicsValue("Acceleration cannot be negative")
        return m*a 
    
def main():
    calculator = PhysicsCalculator()
    try:
        m = float(input("m= "))
        a = float(input("a= "))

        F = calculator.calculate_force(m,a)

        with open('results.txt','a') as f:
            f.write(f"m={m}, a={a}, F={F}")
        
        logging.info(f"calculated force: m={m}, a={a}, F={F}")
        print(f"force={F}")
    
    except ValueError:
        logging.error("Invalid numeric error")
        print("Invalid input. Please enter numeric values")
    
    except InvalidPhysicsValue as e:
        logging.error(f"Physics error: {e}")
        print(f"error: {e}")
        

if __name__ == '__main__':
    main()
