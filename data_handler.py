import nltk
from nltk.corpus import stopwords
import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

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


def split_headline_3_file():
    # Equally split the headlines in headlines_3.txt and write half into two different files
    headlines = []
    print('Extracting headlines...')
    with open('data\headlines3.txt', 'r') as file:
        for line in file:
            headlines.append(line.strip())
    print('Headlines extracted successfully!')
    print('Number of headlines extracted:', len(headlines))
    with open('data\headlines3_annotated_1.txt', 'w') as file:
        for i in range(len(headlines)//2):
            words = headlines[i].split()
            for word in words:
                file.write(word)
            file.write('\n')
    with open('data\headlines3_annotated_2.txt', 'w') as file:
        for i in range(len(headlines)//2, len(headlines)):
            words = headlines[i].split()
            for word in words:
                file.write(word)
            file.write('\n')
    
def aggregate_annotated_data():
    # Aggregate the annotated data from the three files into one file -> annotated_data.txt
    annotated_data = []
    headlines_count = 0
    with open('data\headlines_1_annotated.txt', 'r') as file:
        for line in file:
            if line == '\n':
                headlines_count += 1
            annotated_data.append(line.strip())
    with open('data\headlines_2_annotated.txt', 'r') as file:
        for line in file:
            annotated_data.append(line.strip())
    with open('data\headlines_3_annotated.txt', 'r') as file:
        for line in file:
            annotated_data.append(line.strip())
    with open('data\\annotated_data.txt', 'w') as file:
        for line in annotated_data:
            file.write(line + '\n')
    print('Annotated data aggregated successfully!')
    print('Number of annotated headlines:', len(annotated_data))

def split_annotated_data():
    # Split the data in the annotated_data.txt file into training, validation, and test datasets
    # Do a 50-50-50 split
    raw_data = []
    with open('data\\annotated_data.txt', 'r') as file:
        for line in file:
            raw_data.append(line.strip())

    with open('data\\train_data.txt', 'w') as file:
        for line in raw_data[:50]:
            file.write(line + '\n')
    with open('data\\val_data.txt', 'w') as file:
        for line in raw_data[50:100]:
            file.write(line + '\n')
    with open('data\\test_data.txt', 'w') as file:
        for line in raw_data[100:]:
            file.write(line + '\n')
    


def convert_data_to_csv():
    # Convert the annotated data to a csv file
    # There will be three columns in the csv file: Headline ID, Entity, and Annotation
    annotated_data = []
    headlines_count = 0
    with open('data\\annotated_data.txt', 'r') as file:
        for line in file:
            annotated_data.append(line.strip())
    headline_numbers = []
    entities = []
    annotations = []
    for line in annotated_data:
        if line == '\n' or line == '</s>' or line == "":
            continue
        if line == '<s>':
            headlines_count += 1
            continue
        line = line.split()
        headline_numbers.append(headlines_count)
        print(line)
        entities.append(line[0])
        annotations.append(line[1])
    data = {'Headline Number': headline_numbers, 'Entity': entities, 'Annotation': annotations}
    df = pd.DataFrame(data)
    df.to_csv('data\\annotated_data.csv', index=False)
    print('Data converted to csv successfully!')

def graph_label_counts():
    # Import the .csv file 
    dataframe = pd.read_csv('/content/annotated_data.csv', sep=',')
    dataframe = dataframe.set_index('Headline Number')
    # Make a count of each annotation and store in a dictionary with the key being a unique annotation in the dataframe and the associated value being the count
    label_count = {}
    for ind, val in dataframe.iterrows():
    # print(val['Entity'])
        if label_count.get(val['Annotation'], None):
            label_count[val['Annotation']] += 1
        else:
            label_count[val['Annotation']] = 1
    # Plot the graph
    plt.bar(label_count.keys(), label_count.values())
    
    

def main():
    # headlines = extract_headlines()
    # headlines = clean_headlines(headlines)
    # store_cleaned_headlines(headlines)
    # seperate_headlines(headlines)
    # split_headline_3_file()
    # aggregate_annotated_data()
    # convert_data_to_csv()
    split_annotated_data()

main()