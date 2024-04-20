import nltk
from nltk.corpus import stopwords

def extract_headlines():
    # Extract headlines from the headlines.txt file created by the file_handler.py script
    # Store them in a list and return them
    headlines = []
    print('Extracting headlines...')
    with open('headlines.txt', 'r') as file:
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
    with open('cleaned_headlines.txt', 'w') as file:
        for headline in headlines:
            # have a word per line
            words = headline.split()
            for word in words:
                file.write(word + '\n')
            # add a newline after each headline
            file.write('\n')
    print('Cleaned headlines stored successfully!')

def seperate_headlines(headlines):
    # Seperate the first 150 headlines in the array into three different .txt files
    # The first file contains the first 50 headlines, the second file contains the next 50 headlines, and the third file contains the last 50 headlines
    print('Seperating headlines...')
    with open('headlines1.txt', 'w') as file:
        for i in range(50):
            # have a word per line
            words = headlines[i].split()
            for word in words:
                file.write(word + '\n')
            # add a newline after each headline
            file.write('\n')
    with open('headlines2.txt', 'w') as file:
        for i in range(50, 100):
            # have a word per line
            words = headlines[i].split()
            for word in words:
                file.write(word + '\n')
            # add a newline after each headline
            file.write('\n')
    with open('headlines3.txt', 'w') as file:
        for i in range(100, 150):
            # have a word per line
            words = headlines[i].split()
            for word in words:
                file.write(word + '\n')
            # add a newline after each headline
            file.write('\n')
    print('Headlines seperated successfully!')
        

def main():
    headlines = extract_headlines()
    headlines = clean_headlines(headlines)
    store_cleaned_headlines(headlines)
    seperate_headlines(headlines)

main()