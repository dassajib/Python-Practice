from sys import argv

script, name = argv
name = input('whats your name? -')

prompt = '-'
print(f'Hi mr {name}, I am {script}.')
print(f'I want to know few things.Do you like me {name}?')
likes = input(prompt)

print(f'How old are you {name}?')
Age = input(prompt)

print(f'What do you do {name}?')
Occu = input(prompt)

print(f'Where you live in {name}?')
live = input(prompt)

print(f'what is your goal {name}?')
goal = input(prompt)


print(f'''So you are {name}.
you said some times ago that you{likes} me.
you are {Age}.
you live in {live}
you are {Occu}.
you wanna be {goal}.''')