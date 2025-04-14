import re

# Write a Python regular expression that matches a 10-digit phone number with hyphens.
text = "Contact: alice@example.com, bob123@gmail.com, 2023-10-15, 1-2-3-4-5-6-7-8-9-0"

number = re.search(r'\d-\d-\d-\d-\d-\d-\d-\d-\d-\d', text)

print(number)
print(number.group())


# Write a Python regular expression that matches a street address with a number and a street name, followed by ST or AVE.

address = "123 Main St, 456 Elm Ave, 789 Oak Blvd"
pattern = re.findall(r'\b\d+\s*[A-Za-z]+\s*(?:St|Ave)\b', address, re.IGNORECASE)
print(pattern)


# Write a Python regular expression that matches a full name with any common title like Mr or Mrs followed by any number of names beginning with capital letters, possibly with hyphens between some names.

names = "Mr John Doe, Mrs Jane Smith-Jones, Dr Emily Davis"
name_pattern = re.findall(r'\b(?:Mr|Mrs)\s+[A-Z][a-z]+(?:-[A-Z][a-z]+)*\b', names)
print(name_pattern)


def ahead(file_name, no_of_lines, write_file_name=None):
    # """
    # This function reads a file and writes the first n lines to another file.
    # :param file_name: The name of the file to read from.
    # :param no_of_lines: The number of lines to read.
    # :param write_file_name: The name of the file to write to.
    # """
    # with open(file_name, 'r') as f:
    #     lines = f.readlines()
    #     if write_file_name is not None:
    #         with open(write_file_name, 'w') as w:
    #             for line in lines:
    #                 w.write(line)
    #     else:
    #         print(lines)

    reader = open(file_name, 'r')
    for i in range(no_of_lines):
        line = reader.readline()
        if write_file_name is not None:
            writer = open(write_file_name, 'a')
            writer.write(line)
            writer.close()
        else:
            print(line)
    reader.close()
ahead('sample.txt', 5)
ahead('sample.txt', 5, 'output.txt')



def wordle(word):
    target_word = "apple"
    wrong_words = 0
    correct_words = 0
    exact_matches = {}
    if len(word) != len(target_word):
        return False
    for letter in word:
        if letter in target_word:
            correct_words += 1
        else:
            wrong_words += 1
    for i in range(len(word)):
        if word[i] == target_word[i]:
            print(f"Exact matches at: {i} with {word[i]}")
    print(f"Correct letters: {correct_words}")
    print(f"Wrong letters: {wrong_words}")

print(wordle("apple"))


def check_word(word):
    reader = open('novel.txt')
    no_of_lines = 0
    for line in reader:
        if re.findall(word, line):
            no_of_lines += 1
    reader.close()
    return no_of_lines

print(check_word("pale"))