import string 

occurence = dict.fromkeys(string.ascii_lowercase, 0)  

def number_occurence(text_content):
    for char in text_content.lower():
        if char in occurence:
            occurence[char] += 1

def count_words(text_content):
    return len(text_content.split())

def main():
    with open("books/frankenstein.txt", encoding="utf-8") as f:
        contenu = f.read()
    
    word_count = count_words(contenu)
    
    number_occurence(contenu)
    
    print("\n--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    sorted_occurences = sorted(occurence.items(), key=lambda x: x[1], reverse=True)
    
    for char, count in sorted_occurences:
        print(f"The '{char}' character was found {count} times")
    
    print("\n--- End report ---")

main()
