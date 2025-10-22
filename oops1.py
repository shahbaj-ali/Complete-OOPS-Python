# Initiate a class
class employee:
    # special method/magic method - constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "Data Scientist"

    def travel(self, destination):
        print(f"Employee is travelling to {destination}")

# creating an object of this class
sam = employee()
# print(sam.salary)
sam.travel("Kerala")