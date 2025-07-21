class Drug:
    def __init__(self, name: str, amount: int, price: int):
        self.name = name
        self.amount = amount
        self.price = price


class Pharmacy:
    def __init__(self, name: str):
        self.name = name
        self.drugs = []
        self.employees = []

    def add_drug(self, drug: Drug):
        self.drugs.append(drug)

    def add_employee(self, first_name: str, last_name: str, age: int):
        new_employee = {
            "first_name": first_name.title(),
            "last_name": last_name.title(),
            "age": age
        }
        
        self.employees.append(new_employee)

    def total_value(self) -> int:
        total = 0
        for drug in self.drugs:
            total += drug.amount * drug.price
        return total

    def employees_summary(self) -> str:
        output = 'Employees:\n'
        for i, employee in enumerate(self.employees):
            output += f"The employee number {i + 1} is {employee['first_name']} {employee['last_name']} who is {employee['age']} years old.\n"
        return output
