import os
import yaml
import shelve

print(os.getcwd()) # get the current working directory
print(os.path.abspath('files_and_databases.py')) #this file name gives the exact path of that file
print(os.listdir('python_programming')) # this lists all the contents in that directory
print(os.path.exists('python_programming')) #check if the directory exists, check why it is failing with a file
print(os.path.isdir('python_programming')) #check if the given thing is a directory
print(os.path.isfile('files_and_databases.py')) #check if the given thing is a file, its failing check
print(os.path.join("hi", "hello", "how are you")) #join path with a backslash dependig on the operating system

num_years = 1.5
num_camels = 23
writer = open('camel-spotting-book.txt', 'w')
writer.write(str(num_years))
writer.write(str(num_camels))
a = open('camel-spotting-book.txt').read()
print(a) # why is this not getting printed.

#f-strings

print(f'{num_years} ago, I saw {num_camels}')
config = {
    'photo_dir': 'photos',
    'data_dir': 'photo_info',
    'extensions': ['jpg', 'jpeg'],
}

config_file_name = 'config.yaml'
writer = open(config_file_name, 'w')
yaml.dump(config, writer, sort_keys=False)
writer.close()

readback = open(config_file_name).read()
print(readback)

config_readback = yaml.safe_load(readback)
print(config_readback)

db_file = os.path.join('python_programming', 'captions')
db = shelve.open(db_file, 'c')

key = 'jan-2023/photo1.jpg'
db[key] = 'Cat nose'

print(db[key])

db.close()



word_list = ['opts', 'post', 'pots', 'spot', 'stop', 'tops', 'listen', 'silent', 'enlist', 'tinsel', 'inlets']
word_set = set()

def sorted_key(words):
    for word in words:
        word_set.add("".join(sorted(word)))

sorted_key(word_list)

db = shelve.open('anagram_map', 'n')

for item in word_set:
    value = []
    for i in word_list:
        if "".join(sorted(i)) == item:
            value.append(i)
    db[item] = value

for key in db:
    print(f"{key}: {db[key]}")

db.close()
