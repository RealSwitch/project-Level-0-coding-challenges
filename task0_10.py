def common_characters(string_1, string_2):
    common_characters = list(set(character for character in
                                 string_1.lower() if character
                                 in string_2.lower()
                                 )
                             )

    common_characters = sorted(common_characters)
    print(f"Common letters: {', '.join(common_characters)}")


if __name__ == "__main__":
    common_characters("house", "computers")
    common_characters("hoOuse", "coomputers")
