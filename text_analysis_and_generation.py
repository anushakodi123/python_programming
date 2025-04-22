import random
# def add_bigram(bigram, mapping):
#     first, second = tuple(bigram)
#     if first not in mapping:
#         mapping[first] = [second]
#     else:
#         mapping[first].append(second)


# bigram_map = {}
# add_bigram(("Hi", "Hello"), bigram_map)
# add_bigram(("Hi", "Hey"), bigram_map)

# print(bigram_map)

# successor_map = {}

# def add_bigram(bigram):
#     first, second = bigram
#     successor_map.setdefault(first, []).append(second)
#     return successor_map

# print(add_bigram(("Hi", "Hello")))
# print(add_bigram(("Hi", "hey")))

def clean_word(word):
    return word.strip(punctuation).lower()

successor_map1 = {}
def add_trigram(trigram):
    first, second, third = tuple(trigram)
    successor_map1.setdefault((first, second), []).append(third)
    return successor_map1

# print(add_trigram(["Hi", "Hello", "How are you"]))

window = []
def process_word_trigram(word):
    window.append(word)
    
    if len(window) == 3:
        result = add_trigram(window)
        window.pop(0)
        return result

print(process_word_trigram("anu"))
print(process_word_trigram("sha"))
print(process_word_trigram("hey"))


successor_map = {}
window = []

def add_trigram(trigram):
    first, second, third = trigram
    successor_map.setdefault((first, second), []).append(third)

def process_word_trigram(word):
    window.append(word)
    if len(window) == 3:
        add_trigram(window)
        window.pop(0)

# Simple helpers
def split_line(line):
    return line.split()

def clean_word(word):
    return word.strip('.,!?";:()').lower()

# Test input
text = "The cat sat on the mat".lower()
for word in split_line(text):
    process_word_trigram(clean_word(word))

print(successor_map)



successors = list(successor_map)
bigram = random.choice(successors)


print(bigram[0], bigram[1], end=' ')


