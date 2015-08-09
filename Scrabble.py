def get_list(filepath):
    return open(filepath).read()

print (get_list('words.txt'))
