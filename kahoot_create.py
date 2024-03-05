def butterfinger(text,prob=0.1,keyboard='querty'):
	import random		
	from random import randint
	keyApprox = {}
	
	if keyboard == "querty":
		keyApprox['q'] = "qwasedzx"
		keyApprox['w'] = "wqesadrfcx"
		keyApprox['e'] = "ewrsfdqazxcvgt"
		keyApprox['r'] = "retdgfwsxcvgt"
		keyApprox['t'] = "tryfhgedcvbnju"
		keyApprox['y'] = "ytugjhrfvbnji"
		keyApprox['u'] = "uyihkjtgbnmlo"
		keyApprox['i'] = "iuojlkyhnmlp"
		keyApprox['o'] = "oipklujm"
		keyApprox['p'] = "plo['ik"

		keyApprox['a'] = "aqszwxwdce"
		keyApprox['s'] = "swxadrfv"
		keyApprox['d'] = "decsfaqgbv"
		keyApprox['f'] = "fdgrvwsxyhn"
		keyApprox['g'] = "gtbfhedcyjn"
		keyApprox['h'] = "hyngjfrvkim"
		keyApprox['j'] = "jhknugtblom"
		keyApprox['k'] = "kjlinyhn"
		keyApprox['l'] = "lokmpujn"

		keyApprox['z'] = "zaxsvde"
		keyApprox['x'] = "xzcsdbvfrewq"
		keyApprox['c'] = "cxvdfzswergb"
		keyApprox['v'] = "vcfbgxdertyn"
		keyApprox['b'] = "bvnghcftyun"
		keyApprox['n'] = "nbmhjvgtuik"
		keyApprox['m'] = "mnkjloik"
		keyApprox[' '] = " "
	else:
		print('Keyboard not supported.')

	probOfTypoArray = []
	probOfTypo = int(prob * 100)

	buttertext = ""
	for letter in text:
		lcletter = letter.lower()
		if not lcletter in keyApprox.keys():
			newletter = lcletter
		else:
			if random.choice(range(0, 100)) <= probOfTypo:
				newletter = random.choice(keyApprox[lcletter])
			else:
				newletter = lcletter
		# go back to original case
		if not lcletter == letter:
			newletter = newletter.upper()
		buttertext += newletter
	return buttertext

def typo_generator(word, misspellings_txt_path):
    import random
    # Initialize an empty dictionary to store misspellings
    misspellings_dict = {}

    # Read the .txt file and parse misspellings
    with open(misspellings_txt_path, 'r') as file:
        content = file.read().split('$')
        for item in content:
            lines = item.strip().split('\n')
            if lines[0]:
                misspellings_dict[lines[0]] = lines[1:]

    # Check if the word is in the misspellings dictionary
    if word in misspellings_dict:
        # Filter out empty strings and duplicates
        misspelled_options = list(set(filter(None, misspellings_dict[word])))
        if misspelled_options:
            typo = random.choice(misspelled_options)
        else:
            # No misspellings listed, use butterfinger
            typo = butterfinger(word)
    else:
        # Word not found, use butterfinger
        typo = butterfinger(word)

    # Ensure the typo is not the same as the original word
    while typo == word:
        typo = butterfinger(word)  # You might want to limit the number of retries

    return typo

import pandas as pd
import openpyxl
import numpy as np

# Load the CSV file with vocabulary
file_name = input("Enter the file name: ")
schemeAPercent = float(input("Enter the percentage of scheme A (e.g. 0.6): "))
# Get user input for timeLimit
timeLimit = int(input("Enter the time limit for each question. You may enter 5, 10, 20, 30, 60, 90, 120, or 240: "))

wordlist = pd.read_csv(f'{file_name}.csv', header=None)

# Count the words
total_words = len(wordlist)

# Calculate the number of words for each scheme
schemeA_count = int(np.ceil(total_words * schemeAPercent))
schemeB_count = total_words-schemeA_count  # This might be adjusted later as per your requirement

# Initialize the pandas DataFrame for the quiz
columns = ['Question', 'Word 1', 'Word 2', 'Word 3', 'Word 4', 'Time Limit', 'Correct Answer']
quiz_df = pd.DataFrame(columns=columns)

# Assign words to schemeA_words from the beginning of wordlist up to schemeA_count
schemeA_words = wordlist.iloc[:schemeA_count]
# Assign words to schemeB_words starting from schemeA_count until the end of wordlist
schemeB_words = wordlist.iloc[schemeA_count:]

# Chunking schemeA
schemeA_chunk1 = schemeA_words.iloc[:int(np.ceil(schemeA_count // 4))]
schemeA_chunk2 = schemeA_words.iloc[int(np.ceil(schemeA_count // 4)):int(np.ceil(schemeA_count // 4))*2]
schemeA_chunk3 = schemeA_words.iloc[int(np.ceil(schemeA_count // 4))*2:int(np.ceil(schemeA_count // 4))*3]
schemeA_chunk4 = schemeA_words.iloc[int(np.ceil(schemeA_count // 4))*3:]

current_row = 0  # Initialize the row index

for i in range(1, 5):
    for j in range(len(globals()['schemeA_chunk' + str(i)])):
        # Create a new row as a DataFrame
        new_row = pd.DataFrame(columns=columns)
        new_row.at[0, 'Question'] = "Which one is the correct word?"
        new_row.at[0, 'Word ' + str(i)] = globals()['schemeA_chunk' + str(i)].iloc[j, 0]
        
        for p in range(1, 5):
            if p != i:
                random_word = wordlist.sample().iloc[0, 0]  # Assuming the word is in the first column
                while random_word == new_row.at[0, 'Word ' + str(i)]:
                    random_word = wordlist.sample().iloc[0, 0]
                new_row.at[0, 'Word ' + str(p)] = random_word
                
        new_row.at[0, 'Time Limit'] = timeLimit
        new_row.at[0, 'Correct Answer'] = i
        
        # Concatenate the new row to quiz_df
        quiz_df = pd.concat([quiz_df, new_row], ignore_index=True)
# Chunking schemeB
schemeB_chunk1 = schemeB_words.iloc[:int(np.ceil(schemeB_count // 4))]
schemeB_chunk2 = schemeB_words.iloc[int(np.ceil(schemeB_count // 4)):int(np.ceil(schemeB_count // 4))*2]
schemeB_chunk3 = schemeB_words.iloc[int(np.ceil(schemeB_count // 4))*2:int(np.ceil(schemeB_count // 4))*3]
schemeB_chunk4 = schemeB_words.iloc[int(np.ceil(schemeB_count // 4))*3:]

current_row = 0  # Initialize the row index

for i in range(1, 5):
    for j in range(len(globals()['schemeB_chunk' + str(i)])):
        # Create a new row as a DataFrame
        new_row = pd.DataFrame(columns=columns)
        new_row.at[0, 'Question'] = "Which one is spelled right?"
        new_row.at[0, 'Word ' + str(i)] = globals()['schemeB_chunk' + str(i)].iloc[j, 0]
        
        for p in range(1, 5):
            if p != i:
                random_word = typo_generator(new_row.at[0, 'Word ' + str(i)], 'missp.txt')
                new_row.at[0, 'Word ' + str(p)] = random_word
                
        new_row.at[0, 'Time Limit'] = timeLimit
        new_row.at[0, 'Correct Answer'] = i
        
        # Concatenate the new row to quiz_df
        quiz_df = pd.concat([quiz_df, new_row], ignore_index=True)

#quiz_df.to_csv('output_quiz.csv', index=False)
#print('Quiz template created successfully!')

import openpyxl

# Load the workbook
wb = openpyxl.load_workbook('KahootQuizTemplate.xlsx')

# Select the active sheet
ws = wb.active

# Start from row 9, column 2 (which is B9 in Excel)
row_start = 9
col_start = 2

# Iterate over the dataframe
for index, row in quiz_df.iterrows():
    for c in range(len(row)):
        # Write the data to the cell
        ws.cell(row=row_start, column=col_start + c, value=row.iloc[c])
    row_start += 1

# Save the workbook
wb.save(file_name + '_KahootQuizTemplate.xlsx')
print('Quiz template updated successfully!')