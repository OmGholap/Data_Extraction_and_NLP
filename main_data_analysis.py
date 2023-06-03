from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np
import pandas as pd
from nltk.tokenize import RegexpTokenizer  # for removing punctuations
import string
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import cmudict
import re
import os



# set folder path for the scrapped data saved directory before running the code
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
        #tokenize
        words = nltk.word_tokenize(text_file)
        sent = nltk.sent_tokenize(text_file)
        # Remove punctuation from each word
        words = [word for word in words if word not in string.punctuation]
        sent = [word for word in sent if word not in string.punctuation]

        ''' Positive Score'''

        # reading the postive dictionary 
        filename_positive ='MasterDictionary\positive-words.txt'
        with open(filename_positive, 'r' ,encoding="utf-8") as input_file:
            test_file_positive = input_file.read()

        #check for words in positive dictionary
        score_p = []
        positive_score = 0
        for items in words:
            if items in test_file_positive:
                positive_score +=1
                score_p.append(items)
            else : 
                None

        # print(f'postive score : {round(positive_score,3)}')

        ''' Negative Score'''

        #check for words in negactive dictionary
        filename_negative ='MasterDictionary/negative-words.txt'
        with open(filename_negative, 'r' ,) as input_file:
            test_file_negative = input_file.read()

        score_n = []
        negative_score = 0
        for items in words:
            if items in test_file_negative:
                score_n.append(items)
                negative_score -=1
                nscore = negative_score *-1
            else : 
                None
        # print(f'negative score : {round(nscore,3)}')

        ''' Polarity Score'''

        def polarity_score(positive_score,nscore):
            result = ((positive_score-nscore)/ (positive_score+nscore)) + 0.000001
            print(f'the polarity score = {round(result,3)}')
            return result

        # polarity_score(positive_score,nscore)


        ''' Subjectivity Score'''

        def subjectivity__score(positive_score,nscore):
            result = ((positive_score+nscore))/ ((len(words))+0.000001)
            print(f'the subjectivity score = {round(result,3)}')
            return result

        # subjectivity__score(positive_score,nscore)

        ''' Average Sentence Length '''
        # average sentence lenght 
        def avg_sent_len():
            result = (len(words))/(len(sent))
            print(f'avg sent len : {round(result,3)}')
            return result

        # avg_sent_len()

        ''' Percentage of Complex words '''

        # percentage of complex words 

        # Load the CMU pronunciation dictionary
        prondict = cmudict.dict()

        # Define the function to count syllables
        def count_syllables(word):
        #Count the number of syllables in a word using the CMU pronunciation dictionary.
            try:
                # Get the list of possible pronunciations for the word
                pronunciations = prondict[word.lower()]

                # Count the number of syllables in the first pronunciation
                syllable_count = sum([1 for phoneme in pronunciations[0] if phoneme[-1].isdigit()])

                # Return the syllable count
                return syllable_count
            except KeyError:
                return 0
                # Return 0 if the word is not found in the pronunciation dictionary
        # Initialize the count of complex words
        complex_word_count = 0

        # Loop through each word and count the syllables
        for word in words:
            # Check if the word ends in "es" or "ed"
            if word.endswith("es") or word.endswith("ed"):
                continue
            # Count the syllables in the word
            syllable_count = count_syllables(word)
            # If the word has more than 2 syllables, increment the count of complex words
            if syllable_count > 2:
                complex_word_count += 1

        def per_complex(complex_word_count):
            result = complex_word_count/(len(words))
            print(f'percentage of complex words : {round(result,3)}%')
            return result
        # per_complex(complex_word_count)

        ''' Fog Index '''

        def fog_index():
            result = 0.4 * (avg_sent_len() + per_complex(complex_word_count))
            print(f'fog index : {round(result,3)}')
            return result
        # fog_index()

        ''' Average Number of Words Per Sentence '''

        def avg_no_words_per_sent():
            result = len(words)/len(sent)
            print(f'avg_no_words per sent : {round(result,3)}')
            return result
        # avg_no_words_per_sent()

        ''' Complex Word Count '''

        def com_count(syllable_count):
            result = syllable_count
            print(f'complex words count : {round(result,3)}')
            return result
        # com_count(syllable_count)

        ''' Word Count '''
        with open('D:/Om data/Intership/Blackcoffer/Task 1/Blackcoffer/stopwords.txt', 'r') as stopwords_file:
            stopwords = stopwords_file.read().splitlines()
        with open(path, 'r',encoding="utf-8") as input_file:
            text = input_file.read()
        filtered_text = ' '.join([word for word in text.split() if word.lower() not in stopwords])
        clean_words = nltk.word_tokenize(filtered_text)
        def word_count():
            result = len(clean_words)
            print(f'word count : {round(result,3)}')
            return result
        # word_count()

        ''' Syllable Count Per Word '''

        def count_syllables_in_file(): # file_path was in function input
        # define vowels
            vowels = "aeiouy"

            # define exceptions
            exceptions = ["es", "ed"]

            file_path = path
            # open file
            with open(file_path,"r",encoding="utf-8") as file:
                text = file.read()

            # split text into words
            words = text.split()

            # count syllables per word
            syllables_per_word = []
            for word in words:
                syllables = 0
                prev_char = ""
                for char in word:
                    if char.lower() in vowels and prev_char.lower() not in vowels:
                        syllables += 1
                    prev_char = char
                for exception in exceptions:
                    if word.endswith(exception):
                        syllables -= 1
                        break
                syllables_per_word.append(syllables)

            # calculate average syllables per word
            total_syllables = sum(syllables_per_word)
            num_words = len(words)
            if num_words > 0:
                avg_syllables_per_word = total_syllables / num_words
            else:
                avg_syllables_per_word = 0

            print(f'avg_syllables_per_word : {round(avg_syllables_per_word,3)}')
            return avg_syllables_per_word
        # count_syllables_in_file()        

        ''' Personal Pronouns '''

        import re

        # set path to text file
        file_path = path

        # define regular expression to match personal pronouns
        pronoun_regex = r"\b(I|we|my|ours|us)\b"

        # open text file and read contents
        with open(file_path, "r",encoding = "utf-8") as file:
            text = file.read()

        # count number of personal pronouns in text (excluding "US")
        pronoun_count = len(re.findall(pronoun_regex, text, flags=re.IGNORECASE)) - text.lower().count("us")

        # print result
        print("Personal pronouns (excluding 'US') found in", file_path, ":", pronoun_count)


        ''' Average Word Length '''

        def avg_word_len():
            filename = path
            with open(filename,'r',encoding="utf-8") as f:
                w = [len(word) for line in f for word in line.rstrip().split(" ")]
                w_avg = sum(w)/len(w)
                # print(f'avg word length : {round(w_avg,3)}')
        # avg_word_len()

        print(f'Name of the file : {name_of_file}')
        print("----------------------------------------------------------------")





        
