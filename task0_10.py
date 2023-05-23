def common_characters(string_1,string_2):
    common_characters = []
    for character in string_1:
        if character in string_2:
            common_characters.append(character)
    print("Common letters:",",".join(common_characters))

if __name__ == "__main__":
    common_characters("house","computers")
