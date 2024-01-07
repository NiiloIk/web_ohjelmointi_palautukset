from html.parser import HTMLParser
from urllib.request import urlopen, urlretrieve
from urllib.error import URLError
import re

dangerous_word_list = ['bomb', 'terrorist', 'terrorism', 'kill', 'murder', 'terror']

class MyHTMLParser(HTMLParser):
    amount_of_dangerous_words = 0

    def handle_data(self, data):
        word_amount = len(re.findall(
            r'\b('+"|".join(dangerous_word_list)+r')\b', data, flags=re.IGNORECASE)) # Dangerous words are taken from a list
        if word_amount:
            self.amount_of_dangerous_words += word_amount


parser = MyHTMLParser()


def save_file(link, filepath):
    try:
        urlretrieve(link, filepath)
    except OSError as e:
        print("Failed to load", e)


def get_words_text(link):
    """Tries to open the link provided and searches for the amount of dangerous words. 
    If URL doesn't exist, returns None. If the file cannot be decoded it returns a complaint."""
    try:
        with urlopen(link) as f:
            data = f.read()
            parser.feed(data.decode("utf-8"))
    except URLError:
        return None
    except UnicodeDecodeError:
        return "Doesn't appear to be a HTML file with utf-8 encoding."
    else:
        return "Contains " + str(parser.amount_of_dangerous_words) + " dangerous words."

while True:
    parser.amount_of_dangerous_words = 0

    while True:
        link = input("Input url: ")
        if link:
            break
        print("Not valid url")

    word_text = get_words_text(link)
    if not word_text:
        print("URL doesn't exist")
        continue
    print(word_text)

    while True:
        filepath = input("Input a valid path to save the contents: ")
        if filepath:
            save_file(link, filepath)
            break
        elif filepath == "":
            break
