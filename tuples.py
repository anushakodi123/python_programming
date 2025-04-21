email = 'monty@python.org'
user_name, domain = email.split('@')

print(user_name, domain)


t = ("string", [1,2,3])
t[1].append(678)
print(t[1])

list0 = [1, 2, 3]
list1 = [4, 5]
t = (list0, list1)

t[1].append(6)

print(t)


def shift_word(word, number):
    alphabets="abcdefghijklmnopqrstuvwxyz"
    alpha_numbers = range(len(alphabets))
    map_dic = dict(zip(alphabets, alpha_numbers))
    reverse_map_dic = dict(zip(alpha_numbers, alphabets))
    index_word = []
    list_word = []
    for i in word:
        index = map_dic[i] + number
        index_word.append(index)
    for i in index_word:
        list_word.append(reverse_map_dic[i])
    return ''.join(list_word)


print(shift_word('anusha', 1))


def most_frequent_letters(word):
    word = word.strip().replace(" ", "")
    word_frequency = {}
    for i in word:
        word_frequency[i] = word_frequency.get(i, 0) + 1
    word = sorted(word_frequency.items(), key= lambda item: item[1], reverse=True)
    return dict(word).keys()

print(most_frequent_letters("hello world"))


word_list = ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled', 'retainers', 'ternaries']
sorted_word_list = []
result = {}
values_list = []
for i in word_list:
    sorted_word_list.append("".join(sorted(i)))
unique_list = set(sorted_word_list)
for i in word_list:
    for j in unique_list:
        sorted_word = "".join(sorted(i))
        if j == sorted_word:
            values_list.append(i)
            result[j] = values_list


print(result)