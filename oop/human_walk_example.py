

#Human class walking simulation

class Human:
    def __init__(self, name, steps):
        self.name = name
        self.steps = steps

    def walk(self):
        for i in range(1, self.steps + 1):
            if i == 1:
                print(f"{self.name} started walking...")
            else:
                print(f"{self.name} walked step {i}")

khushi = Human("khushi", 3)
khushi.walk()