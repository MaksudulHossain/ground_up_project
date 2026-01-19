import csv
from physics import PhysicsCalculator, InvalidPhysicsValue 
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s -%(message)s"
)

def main():
    calc = PhysicsCalculator()

    try:
        with open('input_data.csv',newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                formula = row['formula'].strip().lower() 
                try:
                    if formula == 'force':
                        m = float(row['m'])
                        a = float(row['a'])
                        result = calc.calculate_force(m,a)

                    elif formula == 'weight':
                        m = float(row['m'])
                        result = calc.weight(m)
                    
                    elif formula == 'kinetic_energy':
                        m = float(row['m'])
                        v = float(row['v'])
                        result = calc.kinetic_energy(m,v)
                    else:
                        print(f"unknown formula: {formula}")
                        continue 

                    with open("result.txt","a") as f:
                        f.write(f"{formula} result: {result}\n")

                except InvalidPhysicsValue as e:
                    logging.error(f"Physics error: {e}")
                    print(f"error in row {row}: {e}")

    except FileNotFoundError:
        logging.error("CSV file not found")
        print("CSV file not found")

if __name__ == '__main__':
    main()
