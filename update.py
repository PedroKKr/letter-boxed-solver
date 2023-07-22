import json
import re
import requests

url = "https://www.nytimes.com/puzzles/letter-boxed"
response = requests.get(url).text

gameData = json.loads(re.search('window.gameData = (.*)</script></div><div ', response).group(1))

dictionary = [line.strip() for line in open("dictionary.txt")]
dictionary2 = gameData['dictionary']

dictionary = list(set(dictionary).union(dictionary2))

dictionary.sort()

with open('dictionary.txt','w') as f:
    for word in dictionary:
        f.write(f'{word}\n')

sides = gameData['sides']
letters = frozenset(''.join(sides))

print("Number of possible words:", len(dictionary2))

solutions = []

for i, word1 in enumerate(dictionary2):
    current_letters = letters.difference(word1)
    if len(current_letters) == 0:
        solutions.append(word1)
    else:
        current_dictionary = [x for x in dictionary2 if x[0] == word1[-1]]
        for word2 in current_dictionary:
            if len(current_letters.difference(word2)) == 0:
                solutions.append((word1,word2))

print(f"Number of 1 or 2-word solutions: {len(solutions)}")
solutions.sort(key=lambda x: len(''.join(x)))
print("Solutions:")
for x in solutions:
    print(len(''.join(x)),', '.join(x),'<ORDER INVARIANT>' if x[0][-1] == x[1][0] and x[1][-1] == x[0][0] else '')

input("\nPress ENTER to close")
