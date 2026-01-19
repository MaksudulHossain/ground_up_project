from physics import PhysicsCalculator, InvalidPhysicsValue 
import logging

def main():
    calc = PhysicsCalculator()

    try:
        choice = input("Choose formula (force/weight/kinetic_energy)").strip().lower()

        if choice=='force':
            m = float(input("m=? "))
            a = float(input("a=? "))
            result = calc.calculate_force(m,a)

        elif choice=='weight':
            m = float(input("m=? "))
            result = calc.weight(m)

        elif choice=='kinetic_energy':
            m = float(input("m=? "))
            v = float(input("v=? "))
            result = calc.kinetic_energy(m,v)
        else:
            print("Invalid choice")
            return 
        with open("results.txt","a") as f:
            f.write(f"choice={choice}, result={result}")

        logging.info(f"{choice} result: {result}")
        print(f"{choice.capitalize()}={result}")

    except ValueError:
        logging.error("Invalid numeric error")
        print("Invalid input. Please enter numeric values.")
    
    except InvalidPhysicsValue as e:
        logging.error(f"Physics error: {e}")
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
