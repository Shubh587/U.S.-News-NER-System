import nltk
from nltk.corpus import stopwords
import random

def extract_headlines():
    # Extract headlines from the headlines.txt file created by the file_handler.py script
    # Store them in a list and return them
    headlines = []
    print('Extracting headlines...')
    with open('data\headlines.txt', 'r') as file:
        for line in file:
            headlines.append(line.strip())
    print('Headlines extracted successfully!')
    print('Number of headlines extracted:', len(headlines))
    return headlines


def clean_headlines(headlines):
    # remove stopwords, punctuation, and convert to lowercase
    stop_words = set(stopwords.words('english'))

    cleaned_headlines = []
    for headline in headlines:
        # Convert to lowercase
        headline = headline.lower()
        # Remove punctuation except periods using replace() method
        headline = headline.replace(',', '')
        headline = headline.replace('!', '')
        headline = headline.replace('?', '')
        headline = headline.replace(':', '')

        # Remove stopwords
        headline = ' '.join([word for word in headline.split() if word not in stop_words])

        # Add start and end tags at the beginning and end of the headline string
        headline = '<s> ' + headline + ' </s>'

        cleaned_headlines.append(headline)
    
    return cleaned_headlines

def store_cleaned_headlines(headlines):
    # store headlines in CoNLL format
    print('Storing cleaned headlines...')
    with open('data\cleaned_headlines.txt', 'w') as file:
        for headline in headlines:
            # have a word per line
            words = headline.split()
            for word in words:
                file.write(word + '\n')
            # add a newline after each headline
            file.write('\n')
    print('Cleaned headlines stored successfully!')

def seperate_headlines(headlines):
    # Seperate a random set of 150 headlines in the array into three different .txt files
    # The first file contains the first 50 headlines, the second file contains the next 50 headlines, and the third file contains the last 50 headlines
    print('Seperating headlines...')
    prev_headlines = [] # store the previous headlines to avoid annotating duplicates
    with open('data\headlines1.txt', 'w') as file:
        i = 0
        while i < 50: # add 50 new headlines to the each file
            # have a word per line
            ind = random.randint(0, len(headlines))
            headline = headlines[ind]
            if headline not in prev_headlines:
                words = headlines[ind].split()
                for word in words:
                    file.write(word + '\n')
                # add a newline after each headline
                file.write('\n')

                prev_headlines.append(headline)
                i += 1
    with open('data\headlines2.txt', 'w') as file:
        j = 0
        while j < 50:
            ind = random.randint(0, len(headlines))
            headline = headlines[ind]
            if headline not in prev_headlines:
                words = headlines[ind].split()
                for word in words:
                    file.write(word + '\n')
                # add a newline after each headline
                file.write('\n')
                
                prev_headlines.append(headline)
                j += 1
    with open('data\headlines3.txt', 'w') as file:
        k = 0
        while k < 50:
            ind = random.randint(0, len(headlines))
            headline = headlines[ind]
            if headline not in prev_headlines:
                words = headlines[ind].split()
                for word in words:
                    file.write(word + '\n')
                # add a newline after each headline
                file.write('\n')
                
                prev_headlines.append(headline)
                k += 1
    print('Headlines seperated successfully!')
        

def main():
    headlines = extract_headlines()
    headlines = clean_headlines(headlines)
    store_cleaned_headlines(headlines)
    seperate_headlines(headlines)

main()