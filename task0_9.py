def vowels_in_the_string(string):
    vowels = ["a","e","i","o","u"]
    vowels_in_string = []
    for character in string:
        if character in vowels:
            vowels_in_string.append(character)
    print("Vowels:",",".join(vowels_in_string))

if __name__ == "__main__":
    vowels_in_the_string("Umuzi")
    vowels_in_the_string("Amaized")
