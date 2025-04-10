from doctest import run_docstring_examples

def uses_any_incorrect(word, letters):
    for letter in word:
        if letter in letters:
            return True
        else:
            return False
        
print(uses_any_incorrect("hello", "aeiou"))


def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.
    
    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('apple', 'efpg')
    True
    """

    for letter in word:
        if letter in forbidden:
            return True
    return False


print(uses_none("banana", "xyz"))

def run_doctests(func):
    run_docstring_examples(func, globals(), name="doctest", optionflags=0)

print(run_doctests(uses_none))


def uses_any_incorrect(word, letters):
    """Checks if a word uses any of a list of letters.
    
    >>> uses_any_incorrect('banana', 'aeiou')
    True
    >>> uses_any_incorrect('apple', 'xyz')
    False
    """
    for letter in word.lower():
        if letter in letters.lower():
            return True
        else:
            return False     # INCORRECT!
        

run_doctests(uses_any_incorrect)


def uses_only(word, available):
    """Checks whether a word uses only the available letters.
    
    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    """
    for letter in word:
        if letter not in available:
            return False
    return True
print(uses_only("banana", "ban"))


def check_word(word, available, required):
    """Check whether a word is acceptable.
    
    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    if len(word) < 4 or len(word) > 7:
        return False
    for letter in word:
        if letter not in available.lower():
            return False
    if required.lower() not in word.lower():
        return False
    return True


print(run_doctests(check_word))


def word_score(word, available):
    """Compute the score for an acceptable word.
    
    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """
    
    score = 0
    if len(word) <= 4:
        if word not in available:
            score = 0
        score = 1
    else:
        if word not in available:
            score = 0
        score = len(word)





