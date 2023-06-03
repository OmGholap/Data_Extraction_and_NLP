# # #  combining and removing the stop words from 37 text file 

# #     # read in stopwords list file
# # with open('Task 1\Blackcoffer\stopwords.txt', 'r') as stopwords_file:
# #     stopwords = stopwords_file.read().splitlines()

# # # read in file
# # with open('Task 1/Blackcoffer/37.txt', 'r',encoding="utf-8") as input_file:
# #     text = input_file.read()

# # # remove stop words
# # filtered_text = ' '.join([word for word in text.split() if word.lower() not in stopwords])

# # # write filtered text to new file
# # with open('Task 1/Blackcoffer/filtered_37.txt', 'w', encoding="utf-8" ) as output_file:
# #     output_file.write(filtered_text)


# import os

# # define functions
# def count_syllables(word):
#     # implementation here
#     pass

# def count_personal_pronouns(text):
#     # implementation here
#     pass

# def sum_word_lengths(text):
#     # implementation here
#     pass






# # scores (positive negative polarity subjectivity)
# # with open('filtered_37.txt', 'r',encoding="utf-8") as input_file:
# #     test_file = input_file.read('filtered_37.txt')

# from nltk.tokenize import sent_tokenize, word_tokenize
# import numpy as np
# import pandas as pd
# from nltk.tokenize import RegexpTokenizer  # for removing punctuations
# import string
# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# from nltk.corpus import cmudict


# filename = 'filtered_37.txt'  # Replace with the filename of your text file

# with open(filename, 'r' ,encoding="utf-8") as input_file:
#     test_file = input_file.read()

# # print(test_file)
# # print(word_tokenize(test_file))

# #remove punctuation 


# # Open the text file

# # Tokenize the text into individual words
# words_37 = nltk.word_tokenize(test_file)
# sent_37 = nltk.sent_tokenize(test_file)

# # Remove punctuation from each word
# words_37 = [word for word in words_37 if word not in string.punctuation]
# sent_37 = [word for word in sent_37 if word not in string.punctuation]
# # print(sent_37)
# # print(words)
# # Combine the words into a new text without punctuation
# # new_text = ' '.join(words)

# # # Write the new text to a file
# # with open('new_textfile.txt', 'w') as file:
# #     file.write(new_text)

# # print(type(words))
# # print(len(words))

# # reading the postive dictionary 

# filename_positive ='MasterDictionary\positive-words.txt'
# with open(filename_positive, 'r' ,encoding="utf-8") as input_file:
#     test_file_positive = input_file.read()

# # print(test_file_positive)

# #check for words in positive dictionary
# score_p = []
# positive_score = 0
# for items in words_37:
#     if items in test_file_positive:
#         positive_score +=1
#         # print(f'{items} : present in positive dictionary')
#         score_p.append(items)
        
#     else : 
#         # print(f'{items} : not present ')
#         None


# #check for words in negactive dictionary

# filename_negative ='MasterDictionary/negative-words.txt'
# with open(filename_negative, 'r' ,) as input_file:
#     test_file_negative = input_file.read()

# score_n = []
# negative_score = 0
# for items in words_37:
#     if items in test_file_negative:
#         score_n.append(items)
#         negative_score -=1
#         nscore = negative_score *-1
#         # print(f'{items} : present in negative dictionary')
        
#     else : 
#         # print(f'{items} : not present ')
#         None

# print(f'negative score : {nscore}')
# # print(f'lenght of  score_n : {len(score_n)}')
# print(f'postive score : {positive_score}')



# # polarity score calculate 

# score_polarity = []

# def polarity_score(positive_score,nscore):
#     result = ((positive_score-nscore)/ (positive_score+nscore)) + 0.000001
#     print(f'the polarity score = {result}')
#     return result

# polarity_score(positive_score,nscore)

# def subjectivity__score(positive_score,nscore):
#     result = ((positive_score+nscore))/ ((len(words_37))+0.000001)
#     print(f'the subjectivity score = {result}')
#     return result

# subjectivity__score(positive_score,nscore)


# # average sentence lenght 
# def avg_sent_len():
#     result = (len(words_37))/(len(sent_37))
#     print(f'avg sent len : {result}')
#     return result

# avg_sent_len()


# # percentage of complex words 

# # Load the CMU pronunciation dictionary
# prondict = cmudict.dict()

# # Define the function to count syllables
# def count_syllables(word):
#     """
#     Count the number of syllables in a word using the CMU pronunciation dictionary.
#     """
#     try:
#         # Get the list of possible pronunciations for the word
#         pronunciations = prondict[word.lower()]

#         # Count the number of syllables in the first pronunciation
#         syllable_count = sum([1 for phoneme in pronunciations[0] if phoneme[-1].isdigit()])

#         # Return the syllable count
#         return syllable_count
#     except KeyError:
#         # Return 0 if the word is not found in the pronunciation dictionary
#         return 0


# # Initialize the count of complex words
# complex_word_count = 0

# # Loop through each word and count the syllables
# for word in words_37:
#     # Check if the word ends in "es" or "ed"
#     if word.endswith("es") or word.endswith("ed"):
#         continue
#     # Count the syllables in the word
#     syllable_count = count_syllables(word)
#     # If the word has more than 2 syllables, increment the count of complex words
#     if syllable_count > 2:
#         complex_word_count += 1

# # Print the result
# # print("Number of complex words:", complex_word_count)

# def per_complex(complex_word_count):
#     result = complex_word_count/(len(words_37))
#     print(f'percentage of complex words : {result}%')
#     return result
# per_complex(complex_word_count)


# # calculate the fog index 

# def fog_index():
#     result = 0.4 * (avg_sent_len() + per_complex(complex_word_count))
#     print(f'fog index : {result}')
#     return result
# fog_index()

# def avg_no_words_per_sent():
#     result = len(words_37)/len(sent_37)
#     print(f'avg_no_words per sent : {result}')
#     return result
# avg_no_words_per_sent()

# def com_count(syllable_count):
#     result = syllable_count
#     print(f'complex words count : {result}')
#     return result
# com_count(syllable_count)

# def word_count():
#     result = len(words_37)
#     print(f'word count : {result}')
#     return result
# word_count()

# def syllables_count(): # file_path was in function input
#     # define vowels
#     vowels = "aeiouy"

#     # define exceptions
#     exceptions = ["es", "ed"]

#     file_path = 'filtered_37.txt'
#     # open file
#     with open(file_path, "r",encoding="utf-8") as file:
#         text = file.read()

#     # split text into words
#     words = text.split()

#     # count syllables per word
#     syllables_per_word = []
#     for word in words:
#         syllables = 0
#         prev_char = ""
#         for char in word:
#             if char.lower() in vowels and prev_char.lower() not in vowels:
#                 syllables += 1
#             prev_char = char
#         for exception in exceptions:
#             if word.endswith(exception):
#                 syllables -= 1
#                 break
#         syllables_per_word.append(syllables)

#     # calculate average syllables per word
#     total_syllables = sum(syllables_per_word)
#     num_words = len(words)
#     if num_words > 0:
#         avg_syllables_per_word = total_syllables / num_words
#     else:
#         avg_syllables_per_word = 0

#     print(f'avg_syllables_per_word : {round(avg_syllables_per_word,2)}')
#     return avg_syllables_per_word

# syllables_count()


import re
import os
folder_path = "D:/Om data/Intership/Blackcoffer/Task 1/Blackcoffer/content2"
# iterate over files in folder
for filename in os.listdir(folder_path):
    print(filename)
    name_of_file = filename
    # read text file
    path = (folder_path + '/'+ filename)
    print(path)
    with open(path, 'r' ,encoding="utf-8") as file:
        text_file = file.read()

        def count_personal_pronouns(text):
            # define regex pattern for personal pronouns
            pattern = r"\b(I|we|my|ours|us)\b"

            # find all matches of pattern in text
            matches = re.findall(pattern, text, re.IGNORECASE)

            # count number of matches excluding "us"
            count = 0
            for match in matches:
                if match.lower() != "US":
                    count += 1
            
            return count

        filename = path  # Replace with the filename of your text file

        with open(filename, 'r' ,encoding="utf-8") as input_file:
            text = input_file.read()
        # print(text)
        count = count_personal_pronouns(text)
        print(f'Number of personal pronouns: {count}')

#     ''' Average Word Length '''

#     def avg_word_len():
#         filename = '37.txt'
#         with open(filename,'r',encoding="utf-8") as f:
#             w = [len(word) for line in f for word in line.rstrip().split(" ")]
#             w_avg = sum(w)/len(w)
#             print(f'avg word length : {w_avg}')
#     avg_word_len()
#     # set folder path
#     folder_path = "content2"
#     # iterate over files in folder
#     for filename in os.listdir(folder_path):
#         # check if file is a text file
#         if filename.endswith(".txt"):
#             # read text file
#             with open(os.path.join(folder_path, filename), "r" , encoding="utf-8") as file:
#                 text = file.read()

#             # # call functions
#             # syllables = sum(count_syllables(word) for word in text.split())
#             # personal_pronouns = count_personal_pronouns(text)
#             # word_lengths = sum_word_lengths(text)

#             # # print results
#             # print("File:", filename)
#             # print("Number of syllables:", syllables)
#             # print("Number of personal pronouns:", personal_pronouns)
#             # print("Sum of total number of characters in each word:", word_lengths)
#             # print()

# def avg_word_len():
#     filename = '37.txt'
#     with open(filename,'r',encoding="utf-8") as f:
#         w = [len(word) for line in f for word in line.rstrip().split(" ")]
#         w_avg = sum(w)/len(w)
#         print(f'avg word length : {w_avg}')
# avg_word_len()

# # set folder path
# folder_path = "/path/to/folder"

# # # iterate over files in folder
# # for filename in os.listdir(folder_path):
# #     # check if file is a text file
# #     if filename.endswith(".txt"):
# #         # read text file
# #         with open(os.path.join(folder_path, filename), "r") as file:
# #             text = file.read()

# #         words = nltk.word_tokenize(text)
# #         sent = nltk.sent_tokenize(text)

# #         # Remove punctuation from each word
# #         words = [word for word in words_37 if word not in string.punctuation]
# #         sent = [word for word in sent_37 if word not in string.punctuation]


