def vowels_in_the_string(string):
    vowels = ["a", "e", "i", "o", "u"]
    vowels_in_string = []
    for character in string.lower():
        if character in vowels and character not in vowels_in_string:
            vowels_in_string.append(character)
    print(f"Vowels: {','.join(vowels_in_string)}")


if __name__ == "__main__":
    vowels_in_the_string("Umuzi")
    vowels_in_the_string("Amazed")
    vowels_in_the_string("Omega")
