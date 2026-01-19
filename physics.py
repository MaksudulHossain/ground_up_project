import logging 

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s -%(message)s"
)

class PhysicsCaluslator:
    def calculate_force(self, m, a):
        return m*a 
