full_name = "Taylor Arndt"
def print_character(character_string):
    for character in character_string:
        print(character)

def print_characters_and_numbers(character_string):
    for index, character in enumerate(character_string):
        print(f"{index} {character}")

print_character(full_name)
print_characters_and_numbers(full_name)