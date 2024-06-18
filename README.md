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
The script first loads the list of words from the .csv file. It then divides the words into two schemes, A and B, based on the user-defined percentage. It then processes the words as per each scheme. Finally, the script saves the quiz in an Excel file, using a template that is compatible with Kahoot.


### Scheme A - Which one is the correct word?
The script fills in the template with 4 words from your list and selects one as the correct answer. It sets the quiz question to "Which one is the correct word?" After uploading the template to Kahoot, you can then add a picture or GIF to this question. 

Example
<img width="1440" alt="Screenshot 2024-06-18 at 13 35 16" src="https://github.com/voldemortsnose/kahootGenerator/assets/63446204/cac982a6-4e00-4706-8a25-530db478a70a">

### Scheme B - Which one is spelled right?
The script generates three misspelled versions of the correct answer. The misspelled versions are generated using a "butterfinger" function, which simulates typos based on the QWERTY keyboard layout, and a "typo_generator" function, which uses a list of common misspellings. The butterfinger function is taken from https://github.com/alexyorke/butter-fingers/tree/master. The question that will be shown to the students is: "Which one is spelled right?"

Example
<img width="1440" alt="Screenshot 2024-06-18 at 13 38 41" src="https://github.com/voldemortsnose/kahootGenerator/assets/63446204/912332eb-ae84-4278-95ce-eee005921f5f">
