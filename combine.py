dictionary = [line.strip() for line in open("dictionary.txt")]
dictionary2 = [line.strip() for line in open("dictionary2.txt")]

dictionary = list(set(dictionary).union(dictionary2))

dictionary.sort()

with open('dictionary.txt','w') as f:
    for word in dictionary:
        f.write(f'{word}\n')
