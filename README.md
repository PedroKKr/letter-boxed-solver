# Letter Boxed Solver
A simple Python solver that finds all 2-word solutions for the game Letter Boxed, and ranks them by the least amount of used letters.

`combine.py` is a file that combines the words from the files `dictionary.txt` and `dictionary2.txt`. The latter is the main dictionary used by the solver, while the former is a new wordlist that includes new words. This is because the dictionary is not yet complete and may need to be updated.

`get_dictionary.js` contains the code that one must run in the console of the browser to download the current Letter Boxed dictionary, that may be combined with `dictionary.txt` to obtain a more complete wordlist. This dictionary is also all the words needed to solve the current game.

To get the sides of the square for the current game, enter `window.gameData.sides` in the browser console
