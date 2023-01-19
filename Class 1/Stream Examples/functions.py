first_name = "Taylor"
last_name = "Arndt"

def print_names():
    print(f"Hello, {first_name} {last_name}")

def combine_words(word_1, word_2):
    return word_1 + " " + word_2

print_names()
full_name = combine_words(first_name, last_name)
print(full_name)