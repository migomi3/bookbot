def generateReport(wordCount, charCount):
    print("--- Begin report of books/frankenstein.txt ---\n")
    print(f"{wordCount} found in document.\n")
    for x in charCount:
        print(f"'{x['name']}' char was used {x['num']} times.")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def dictToLists(char_count):
    countList = []
    for x in char_count:
        countList.append({"name": x, "num": char_count[x]})
    
    return countList


def countChar(book):
    char_count = {}

    lowerCaseBook = book.lower()

    for x in lowerCaseBook:
        if x.isalpha():
            if x not in char_count: char_count[x] = 0
            char_count[x] += 1
    
    return char_count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        wordCount = len(words)

        char_count = countChar(file_contents)
        charList = dictToLists(char_count)
        charList.sort(reverse=True, key=sort_on)

        generateReport(wordCount, charList)

if __name__=="__main__":
    main()