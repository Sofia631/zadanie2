def greet(name):
    return f"Привет, {name}!"

def add(a, b):
    return a + b

def is_even(num):
    return num % 2 == 0

def multiply(a, b):
    return a * b

def main():
    print(greet("Пользователь"))
    print("Сумма:", add(10, 20))
    print("Чётное?", is_even(4))
    print("Произведение:", multiply(3, 4))

if __name__ == "__main__":
    main()

