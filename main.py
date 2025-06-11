from os import sep
from stats import get_word_count
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_count = get_char_count(text)
    dict_list = dict_to_listofdicts(char_count)
    dict_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("\n")
    print_pretty_list(dict_list)
    print("\n")
    print("--- End report ---")





def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()



def get_char_count(text: str) -> dict:
    char_count_dict = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_count_dict:
            char_count_dict[lowered_char] = char_count_dict[lowered_char] + 1
        else:
            char_count_dict[lowered_char] = 1
    return char_count_dict

def dict_to_listofdicts(dict: dict) -> list:
    return [{'char': key, 'num': value} for key, value in dict.items()]

def sort_on(dict: dict) -> int:
    return dict["num"]

def print_pretty_list(dict_list: list):
    for dict in dict_list:
        char = dict["char"]
        num = dict["num"]
        if char.isalpha():
            print(f"{char}: {num}")




main()
