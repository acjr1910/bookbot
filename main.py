def main():
    generate_report()

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    xs = text.split()
    return len(xs)

def count_characters(text):
    chars = [x for x in text.lower()]
    charCount = {}

    for char in chars:
        if char.isalpha():    
          if not char in charCount:
              charCount[char] = 1
          else:
              charCount[char] += 1

    return charCount

def print_char_report(char_count):
    for key in char_count:
        print(f"The '{key}' character was found {char_count[key]} times")

def generate_report():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(text)} words found in the document")
    print("")
    print_char_report(count_characters(text))
    print("--- End report ---")

main()