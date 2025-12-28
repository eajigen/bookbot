import sys
from stats import word_count, char_count, get_sorted_items

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    try:
        text = get_book_text(path)
    except FileNotFoundError:
        print(f"Error: Teh file at {book_path} was not found.")
        sys.exit(1)
    
    num_words = word_count(text)
    chars_dict = char_count(text)
    sorted_char_list = get_sorted_items(chars_dict)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for item in sorted_char_list:
        print(f"{item['char']}: {item['num']} ")
    print(f"============= END ===============")
#   print(chars_dict)

main()


