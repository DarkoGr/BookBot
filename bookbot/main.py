#ovde pravimo funkciju koja vraca ceo sadrzaj fajla
from stats import words_count
from stats import char_count
from stats import report


def get_book_text(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print("File not found!")
        return ""
    except Exception as e:
        print("Unecspected error found: {e}")
        return ""


def main():
    tekst = get_book_text("/home/grubic/BookBot/bookbot/books/frankenstein.txt")
    words_num = words_count(tekst)
    char_count_report = char_count(tekst)
    final_report = report(char_count_report)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words_num} total words")
    print("--------- Character Count -------")
    
    for i in final_report:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

    
if __name__ == "__main__":
    main()




