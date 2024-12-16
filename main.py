def get_string(file_content):
    return file_content.split()

def count_words(file_content):
    return len(get_string(file_content))

def number_occurence(text_content):
    occurence = {}
    for lettre in text_content:
        
        if (occurence[lettre]
        occurence[lettre] = 1

def main():
    with open("books/frankenstein.txt") as f:
        contenu = f.read()  
    print(count_words(contenu))

main()