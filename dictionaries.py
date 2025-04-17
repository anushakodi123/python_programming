def value_counts(string):
    counter = {}
    for i in string:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    return counter
print(value_counts("banana"))


def value_countss(string):
    counter = {}
    for i in string:
            counter[i] = counter.get(i, 0) + 1
    return counter

print(value_countss("banana"))


def has_duplicates(string):
  count = {}
  for i in string:
    count[i] = count.get(i, 0) + 1
    
  values = count.values()
  if 2 in values:
    return True
  else:
    return False
  
print(has_duplicates("excursion"))

first_map = value_countss('brontosaurus')
second_map = value_countss('apatosaurus')

print(first_map)
print(second_map)

def add_counters(first_map, second_map):
    final_map ={}
    final_map = first_map
    for i in second_map:
        final_map[i] = final_map.get(i, 0) + 1
    return final_map

print(add_counters(first_map, second_map))

def is_interlocking(word, word_list):
    first_part = word[::2]
    second_part = word[1::2]
    return first_part in word_list and second_part in word_list

print(is_interlocking('schooled', ['school', 'shoe', 'cold', 'banana']))
