# Kahoot Quiz Generator

This Python script generates a Kahoot quiz from a list of words. The words are divided into two schemes, A and B, based on a user-defined percentage. The quiz is then saved in an Excel file. This Excel file can be directly uploaded to Kahoot.

## Requirements

- A .csv file containing the list of words
- A .txt file containing common misspellings. The file can be downloaded from https://www.dcs.bbk.ac.uk/~ROGER/corpora.html (optional)

## How to Use

1. Run the script `kahoot_create.py`.
2. When prompted, enter the name of the CSV file (excl. the .csv ending) containing your list of words.
3. Enter the percentage of words you want to assign to Scheme A. The remaining words will be assigned to Scheme B.
4. Enter the time limit for the questions. You can choose from 5, 10, 20, 30, 60, 90, 120, or 240 seconds.
5. The script will generate the quiz and save it as an Excel file.

## How it works
The script first loads the list of words from the .csv file. It then divides the words into two schemes, A and B, based on the user-defined percentage.

For scheme A, the script generates three random words from the list as incorrect answers. For scheme B, the script generates three misspelled versions of the correct answer as incorrect answers. The misspelled versions are generated using a "butterfinger" function, which simulates typos based on the QWERTY keyboard layout, and a "typo_generator" function, which uses a list of common misspellings. The butterfinger function is taken from https://github.com/alexyorke/butter-fingers/tree/master.

The script then creates a new row in the quiz for each word, with the question "Which one is the correct word?" (Scheme A) or "Which one is spelled right?" (Scheme B), the four answer options, the time limit, and the correct answer.

Finally, the script saves the quiz in an Excel file, using a template that is compatible with Kahoot.
