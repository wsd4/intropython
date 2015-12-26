from pprint import pprint

# list LIFO - append() : pop()
# list FIFO - append() : pop(0)


var1 = 1
var1 = 'str'
print(var1)

print(7 / 2)
print(7 // 2)

var2 = +1234
print(var2)

print(divmod(9, 5))

print(0B1 + 0B111)
print(0X10)

print(int('1234'))
googol = 10**100
print(googol)
print(googol * googol)

bottles = 99
base = ''
base += 'current inventory: "'
base += str(bottles)
base += '"'
print(base)

print('Na' * 30)

name = 'Henny'
print('P' + name[1:])


todos = 'get gloves, get mask, give cat vitamins, call abulance'
print(todos.split())

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)
print(crypto_string.isalnum())
print(crypto_string.ljust(80))
print(crypto_string.center(80))
print(crypto_string.rjust(80))
print(crypto_string.replace('Big', 'Small'))




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




a = {1, 2}
b = {2, 3}
print(a & b)
print(a.intersection(b))
