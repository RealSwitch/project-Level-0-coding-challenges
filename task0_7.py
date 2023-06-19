def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * (9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


if __name__ == "__main__":
    print(celsius_to_fahrenheit(1))
    print(celsius_to_fahrenheit(32))
    print(fahrenheit_to_celsius(1))
    print(fahrenheit_to_celsius(32))
