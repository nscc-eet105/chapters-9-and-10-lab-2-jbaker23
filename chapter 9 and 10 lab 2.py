#My name is Jacob Baker and this is Chapter 9 and 10 Lab 2 which I am completing on July 8
def main():
    filename = input("What is the name of the file?  ")
    try:
        with open(filename, "r") as file:
            content = file.read()

        words = content.split()

        total_words = len(words)

        capitalized_words = sum (words.isupper() for words in words)

        print(f"The file has a number of {total_words} total words in it.")

        print(f"The file has a number of {capitalized_words} capital words in it.")
    except:
        print(f"Sorry, the file {filename} doesn't exist.")


if __name__ == "__main__":
    main()

