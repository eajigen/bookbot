def word_count(text):
    count = text.split()
    return len(count)

def char_count(text):
    chars = {}
    lowercase_string = text.lower()

    for char in lowercase_string:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

def sort_on(dict):
    return dict["num"]

def get_sorted_items(chars_dict):
    sorted_list = []
    for char in chars_dict:
        if char.isalpha():
            new_dict = {"char": char, "num": chars_dict[char]}
            sorted_list.append(new_dict)
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

