def find_maximum(*integers):
    maximum = integers[0]
    for integer in integers:
        if integer > maximum:
            maximum = integer
    return maximum
    
if __name__ == "__main__":
    print(find_maximum(1,2,3,9,9,9))
