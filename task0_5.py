def triangle(side_1,side_2,side_3):
    semi_perimeter = (side_1 + side_2 + side_3)//2
    area = (semi_perimeter*(semi_perimeter - side_1)*(semi_perimeter - side_2)*(semi_perimeter - side_3))**(1/2)
    return area

if  __name__ == "__main__":
    print(triangle(4,5,3))
    print(triangle(1,2,3))
