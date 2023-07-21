dictionary = [line.strip() for line in open("dictionary.txt")]

sides = ["ILP", "URN", "SOA", "HTD"]
letters = frozenset(''.join(sides))

letter_side = {}
for i,side in enumerate(sides):
    for letter in side:
        letter_side[letter] = i

def is_valid_word(word, letter_side):
    for letter1, letter2 in zip(word,word[1:]):
        if letter1 not in letter_side or letter2 not in letter_side or letter_side[letter1] == letter_side[letter2]:
            return False
    return True

dictionary = [word for word in dictionary if is_valid_word(word, letter_side)]
print("Number of possible words:", len(dictionary))

solutions = []

for i, word1 in enumerate(dictionary):
    current_letters = letters.difference(word1)
    current_dictionary = [x for x in dictionary if x[0] == word1[-1]]
    for word2 in current_dictionary:
        if len(current_letters.difference(word2)) == 0:
            solutions.append((word1,word2))

print(f"Number of 2-word solutions: {len(solutions)}")
solutions.sort(key=lambda x: len(''.join(x)))
print("Solutions:")
for x in solutions:
    print(len(''.join(x)),', '.join(x),'<ORDER INVARIANT>' if x[0][-1] == x[1][0] and x[1][-1] == x[0][0] else '')
