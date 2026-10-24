
class Vehicle:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def get_info(self):
        return f"Model: {self.model} | Color: {self.color}"


class Car(Vehicle):
    def __init__(self, model, color, num_of_wheels):
        super().__init__(model, color)
        self.num_of_wheels = num_of_wheels

    def get_info(self):
        parent_info = super().get_info()
        return f"{parent_info} | Number of wheels: {self.num_of_wheels}"


while True:
    model = input('Enter car model (or "exit" to stop): ').strip()

    if model.lower() == "exit":
        break

    color = input("Enter car color: ").strip()
    wheels_input = input("Enter number of wheels: ").strip()

    if not wheels_input.isdigit():
        print("Please enter a valid positive integer.")
        continue

    num_of_wheels = int(wheels_input)

    if num_of_wheels == 0 or num_of_wheels<0:
        print("Number of wheels must be greater than zero.")
        continue

    car = Car(model, color, num_of_wheels)
    print(car.get_info())
