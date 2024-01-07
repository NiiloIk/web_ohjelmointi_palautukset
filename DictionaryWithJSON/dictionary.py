import json
dictionary = {"dog": "koira", "cat": "kissa", "duck": "ankka"}

# Loading dictionary and adding it to our local dictionary
try:
    with open("dictionary.json") as f:
        dictionary = json.loads(f.read())
        print("Dictionary loaded.")
except OSError as e:
    print(f"Failed to open file: {e}\nUsing default dictionary.")


def get_new_word():
    'Get a new word from user and return None if there is no input'
    while True:
        new_word = input(
            "Does not exist. What is this word in Finnish?\nInput empty to skip ").lower()
        if new_word:
            return new_word
        return None


def save_dict_to_json():
    'Save local dictionary to dictionary.json file'
    try:
        with open("dictionary.json", "w") as f:
            json.dump(dictionary, f)
            print("Successfully written!")
    except OSError as e:
        print(f"Failed to save dictionary: {e}")


while True:
    # Ask the user for word input
    word = input("Ask for a word: (enter empty to exit and save)").lower()

    if word in dictionary:  # if the word is in dictionary print it.
        print(f"{word} = {dictionary[word]}")
    elif word == "":  # if user inputs empty, save and exit.
        save_dict_to_json()
        print("goodbye!")
        break
    else:  # If the word doesn't exist, ask for a new input.
        new_word = get_new_word()
        if not new_word:
            continue
        dictionary[word] = new_word
