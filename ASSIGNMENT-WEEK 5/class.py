# ENCAPSULATION: Bundling data and methods together
class Prison:
    def __init__(self, name, capacity):
        # Attributes are encapsulated within the class
        self.name = name
        self.capacity = capacity
        self.inmates = []  # Data hidden from direct access
    
    # Methods provide controlled access to data
    def add_inmate(self, inmate_id, name):
        if len(self.inmates) >= self.capacity:
            return "Prison at capacity."
        
        self.inmates.append({'id': inmate_id, 'name': name})
        return f"Inmate {name} added."
    
    def release_inmate(self, inmate_id):
        for inmate in self.inmates:
            if inmate['id'] == inmate_id:
                self.inmates.remove(inmate)
                return f"Inmate {inmate['name']} released."
        return "Inmate not found."


# INHERITANCE: SupermaxPrison inherits from Prison
class SupermaxPrison(Prison):
    def __init__(self, name, capacity):
        # Call parent constructor
        super().__init__(name, capacity)
        # Add new attribute
        self.escape_attempts = 0
    
    # POLYMORPHISM: Method overriding
    def add_inmate(self, inmate_id, name):
        # Extend parent method functionality
        result = super().add_inmate(inmate_id, name)
        return result + " (High-security protocols applied)"
    
    # New method specific to child class
    def report_escape_attempt(self):
        self.escape_attempts += 1
        return f"Escape attempt #{self.escape_attempts} reported."


# POLYMORPHISM: Function works with any Prison type
def print_status(prison):
    print(f"{prison.name}: {len(prison.inmates)}/{prison.capacity} inmates")


# Demonstration
if __name__ == "__main__":
    # Create instances
    state_pen = Prison("State Penitentiary", 500)
    supermax = SupermaxPrison("ADX Florence", 200)
    
    # Use methods
    print(state_pen.add_inmate(1001, "John Doe"))
    print(supermax.add_inmate(2001, "Frank Morris"))
    print(supermax.report_escape_attempt())
    
    # Demonstrate polymorphism
    prisons = [state_pen, supermax]
    for prison in prisons:
        print_status(prison)