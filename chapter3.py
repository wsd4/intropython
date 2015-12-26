from pprint import pprint

# list LIFO - append() : pop()
# list FIFO - append() : pop(0)

marxes = ['Groucho', 'Chiro', 'Harpo', 'Zepoo']
print('Groucho' in marxes)
print(marxes.count('Chiro'))
print(marxes.count('Bob'))
print(','.join(marxes))

friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)
separated = joined.split(separator)
print(separated)
print(separated == friends)

sorted_marxes = sorted(marxes)
print(sorted_marxes)
print(marxes)
marxes.sort(reverse=True)
print(marxes)
print(marxes.__len__())
print(len(marxes))
pprint(dir(marxes))


marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)
a, b, c = marx_tuple
print(a, b, c)
a, b, c = friends
print(a, b, c)

# 임시 변수 없이 값을 교환
password = 'swordfish'
icecream = 'tuttifrutti'
icecream, password = password, icecream
print(icecream, password)

drinks = {
    'martini':      {'vodka', 'vermouth'},
    'black russian':{'vodka', 'kahlua'},
    'white russian':{'cream', 'kahlua', 'vodka'},
    'manhattan':    {'rye', 'vermouth', 'bitters'},
    'screwdriver':  {'orange juice', 'vodka'}
}

print('\n\n')
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

print('\n\n')
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

print('\n\n')
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)


