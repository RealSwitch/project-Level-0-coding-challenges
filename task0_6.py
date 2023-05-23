def find_maximum(number_1,number_2,number_3):
    if number_1 > number_2 and number_1 > number_2:
        return number_1
    elif number_2 > number_1 and number_2 > number_3:
        return number_2
    elif number_3 > number_1 and number_3 > number_2:
        return number_3

if __name__ == "__main__":
    print(find_maximum(1,2,3))
