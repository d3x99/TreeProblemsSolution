height_of_tree = input('What tree height?')
spaces = int(height_of_tree)
sec_range = 0
char = ''
list_of_char = []
index_of_char = 64
for character in range(int(height_of_tree)):
    sec_range += 1
    for index in range(sec_range):
        index_of_char += 1
        list_of_char.append(chr(index_of_char))
    print(spaces * ' ' + ' '.join(list_of_char))
    spaces -= 1
    list_of_char = []
