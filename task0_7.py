def celsius_to_fehrenheit(celsius):
    fehrenheit = celsius*(9/5)+32
    return fehrenheit

def fehrenheit_to_celsius(fehrenheit):
    celsius = (fehrenheit-32)*(5/9)
    return celsius

if __name__ == "__main__":
    print(celsius_to_fehrenheit(1))
    print(celsius_to_fehrenheit(32))
    print(fehrenheit_to_celsius(1))
    print(fehrenheit_to_celsius(32))
