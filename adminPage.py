import random
import string

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

numbers = [random.randint(1, 100) for _ in range(10)]
squared = list(map(lambda x: x**2, numbers))

print(f"Random String: {random_string()}")
print(f"Fibonacci Sequence: {list(fibonacci(10))}")

dog = Animal("Dog")
print(dog.speak())

with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
