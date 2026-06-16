# We import the 'abc' module (Abstract Base Classes) to implement Abstraction.
from abc import ABC, abstractmethod

# ------------------------------------------------------------------------------
# PILLAR 1: ABSTRACTION
# ------------------------------------------------------------------------------
# Concept: Abstraction hides complex implementation details and only shows the 
# essential features. Think of it like a blueprint or a contract. 
# You cannot create an object directly from an Abstract Class.

class Employee(ABC):  # Inheriting from ABC makes this an Abstract Class
    
    # The Constructor (__init__): Initializes the object's attributes.
    # 'self' represents the specific object instance we are currently creating.
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        
        # ----------------------------------------------------------------------
        # PILLAR 2: ENCAPSULATION
        # ----------------------------------------------------------------------
        # Concept: Bundling data and methods into a single unit, and restricting
        # direct access to some of the object's components to prevent accidental modification.
        #
        # - Single underscore (_variable): 'Protected' (A hint to other devs not to touch it)
        # - Double underscore (__variable): 'Private' (Python actively hides/mangles this)
        
        self.__base_salary = 50000  # Private attribute: cannot be accessed directly outside
        
    # --- GETTER & SETTER (Controlled access to encapsulated data) ---
    @property
    def base_salary(self):
        """Getter: Allows us to read the private salary safely."""
        return self.__base_salary

    @base_salary.setter
    def base_salary(self, amount):
        """Setter: Allows us to modify private salary, but with validation logic!"""
        if amount > 0:
            self.__base_salary = amount
        else:
            print("Error: Salary must be a positive number!")

    # --- ABSTRACT METHOD ---
    # Every child class *must* implement this method, or Python will throw an error.
    @abstractmethod
    def calculate_salary(self):
        pass

    # A regular method that all child classes will automatically share
    def get_details(self):
        return f"ID: {self.emp_id} | Name: {self.name}"


# ------------------------------------------------------------------------------
# PILLAR 3: INHERITANCE
# ------------------------------------------------------------------------------
# Concept: A way to create a new class (Child) using details of an existing class (Parent).
# This promotes code reusability.

class Developer(Employee):  # 'Developer' inherits from 'Employee'
    
    def __init__(self, name, emp_id, programming_language):
        # super() calls the Parent class's constructor to set up name, emp_id, and private variables
        super().__init__(name, emp_id)
        self.programming_language = programming_language
        
    # Implementing the abstract method required by the parent contract
    def calculate_salary(self):
        # Developers get a tech bonus on top of their base salary
        tech_bonus = 15000
        return self.base_salary + tech_bonus


class Manager(Employee):  # 'Manager' also inherits from 'Employee'
    
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size
        
    # --------------------------------------------------------------------------
    # PILLAR 4: POLYMORPHISM
    # --------------------------------------------------------------------------
    # Concept: "Many forms." It allows different classes to have methods with the
    # exact same name but entirely different underlying logic.
    
    # Manager implements the SAME method name as Developer, but calculates it differently!
    def calculate_salary(self):
        # Managers get a bonus based on their team size
        team_bonus = self.team_size * 2000
        return self.base_salary + team_bonus

    # Method Overriding: We are rewriting the parent's 'get_details' to add manager-specific info
    def get_details(self):
        parent_info = super().get_details()
        return f"{parent_info} | Role: Manager | Team Size: {self.team_size}"


# ==============================================================================
# EXECUTION & DEMONSTRATION
# ==============================================================================
print("--- Step 1: Demonstrating Abstraction Error ---")
try:
    # This will FAIL because you cannot instantiate an abstract class directly!
    failed_emp = Employee("Ghost", 999)
except TypeError as e:
    print(f"Successfully blocked instantiation: {e}\n")


print("--- Step 2: Creating Objects (Instances) ---")
# Creating instances of our concrete child classes
dev_1 = Developer("Rahul", 101, "Python")
mgr_1 = Manager("Priya", 102, team_size=5)

print(dev_1.get_details())
print(mgr_1.get_details())
print()


print("--- Step 3: Demonstrating Encapsulation ---")
# Trying to access the private variable directly will crash the program:
# print(dev_1.__base_salary) # -> Raises AttributeError

# Instead, we use the safe Getter property:
print(f"Rahul's original base salary: ${dev_1.base_salary}")

# Using the Setter to change it with validation rules:
dev_1.base_salary = -1000  # Triggers our validation error
dev_1.base_salary = 65000  # Updates successfully
print(f"Rahul's new base salary:      ${dev_1.base_salary}\n")


print("--- Step 4: Demonstrating Polymorphism ---")
# We create a list containing different types of employees
team = [dev_1, mgr_1]

# We can loop through them and call 'calculate_salary' blindly. Python automatically
# triggers the correct version of the method depending on what the object actually is!
for member in team:
    print(f"Total Payout for {member.name}: ${member.calculate_salary()}")

print("==============================================================================")