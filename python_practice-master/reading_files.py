from sys import argv

script, filename = argv
txt = open(filename)

print(f'Here is the file {filename}: ')
print(txt.read())

txt.close

