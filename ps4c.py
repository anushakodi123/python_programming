# Problem Set 4C
# Name:
# Collaborators:

import json
import ps4b

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.
    '''
    with open(file_name, 'r') as inFile:
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise
    '''
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"").lower()
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text (string).
    """
    with open("story.txt", "r") as f:
        story = f.read()
    return story.strip()

def get_story_pads():
    """
    Loads and returns a list of one-time pads (list of list of ints).
    """
    with open('pads.txt') as json_file:
        return json.load(json_file)

WORDLIST_FILENAME = 'words.txt'
### END HELPER CODE ###

def decrypt_message_try_pads(ciphertext, pads):
    word_list = load_words(WORDLIST_FILENAME)
    best_pad = None
    max_valid_words = -1
    best_plaintext = None

    for pad in pads:
        encrypted_msg = ps4b.EncryptedMessage(ciphertext)
        plaintext_obj = encrypted_msg.decrypt_message(pad)
        plaintext_text = plaintext_obj.get_message_text()

        words = plaintext_text.split()
        valid_word_count = sum(is_word(word_list, word) for word in words)

        if valid_word_count >= max_valid_words:
            max_valid_words = valid_word_count
            best_pad = pad
            best_plaintext = plaintext_text

    return ps4b.PlaintextMessage(best_plaintext, best_pad)


def decode_story():
    '''
    Decrypts Bob's encrypted story using the correct one-time pad from list.

    Returns: (string) The decrypted story text.
    '''
    story_cipher = get_story_string()
    pads = get_story_pads()
    decrypted = decrypt_message_try_pads(story_cipher, pads)
    return decrypted.get_message_text()

if __name__ == '__main__':
    story = decode_story()
    print("Decoded story:\n", story)
