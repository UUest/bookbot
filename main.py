def main():
    book_path = "books/frankenstein.txt"
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
    
def get_word_count(text: str) -> int:
    word_list = text.split()
    return len(word_list)

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
            print(f"The '{char}' character was found {num} times")




main()