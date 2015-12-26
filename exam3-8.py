# 3.1
year_lists = [1980, 1981, 1982, 1983, 1984]

# 3.2
print(year_lists[2])

# 3.3
print(year_lists[-1])

# 3.4
things = ["mozzarella", "cinderella", "salmonella"]

# 3.5
for t in things:
    print(t.capitalize())

# 3.6
things[0] = things[0].upper()
print(things)

# 3.7
things.remove("salmonella")
print(things)

# 3.8
surprise = [ "Groucho", "Chico", "Harpo" ]

# 3.9
surprise[-1] = surprise[-1].lower()[::-1].capitalize()
print(surprise[-1])

# 3.10
f2e = {'chien':'dog', 'chat':'cat', 'walrus':'morse' }
print(f2e)

# 3.11
print(f2e['walrus'])

# 3.12
e2f = dict()
for k, v in f2e.items():
    e2f[v] = k
print(e2f)

# 3.13
print(f2e['chien'])

# 3.14
print(list(e2f.keys()))

# 3.15
life = {
    'animals': {
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': {},
        'emus': {}
    },
    'plants': {},
    'other': {}
}

# 3.16
print(list(life.keys()))

# 3.17
print(list(life['animals'].keys()))

# 3.18
print(life['animals']['cats'])

