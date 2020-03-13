f = open('names.txt', 'r')
array_of_strings = f.read().splitlines()
f.close()

dict_of_names = {}
dupes = []

for entry in array_of_strings:
    split_strings = entry.split('|')
    deleted = split_strings[1].strip()

    if deleted != '0':
        continue
    name = split_strings[0].strip()

    if name.lower() in dict_of_names:
        dupes.append(name)
    else:
        dict_of_names[name.lower()] = name


print (dupes)
