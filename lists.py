def is_anagram(input1, input2):
    """
    Check if two strings are anagrams of each other.
    """
    return sorted(input1) == sorted(input2)

print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))


def find_anagrams(word, word_list):
    """
    Find all anagrams of a given word in a list of words.
    """
    return [w for w in word_list if is_anagram(word, w)]
print(find_anagrams("listen", ["enlist", "google", "inlets", "banana"]))
print(find_anagrams("hello", ["world", "helloo", "loleh", "oellh"]))

def is_palindrome(word):
    return word == reverse_word(word)

def reverse_word(word):
    return ''.join(reversed(word))

print(is_palindrome("racecar"))


def reverse_sentence(sentence):
    """
    Reverse the words in a sentence.
    """
    a = ' '.join(reversed(sentence.split())).lower()
    a = a[0].upper() + a[1:]
    return a

print(reverse_sentence("Hello world!"))

def total_length(words):
    """
    Calculate the total length of a list of words.
    """
    return sum(len(word) for word in words)
print(total_length(["hello", "world", "python"]))