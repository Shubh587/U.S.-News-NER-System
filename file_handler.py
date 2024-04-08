# Traverse through the Reuter's dataset in rcv1 and extract the new's headlines from all of the XML files
# and store them in a text file.
import os
import xml.etree.ElementTree as ET

def extract_headlines():
    rootdir = 'rcv1'
    headlines = []
    print('Extracting headlines...')
    for subdir, dirs, files in os.walk(rootdir):
        print('Extracting headlines from:', subdir)
        for file in files:
            # print('Extracting headlines from:', file)
            if file.endswith('.xml'):
                tree = ET.parse(os.path.join(subdir, file))
                root = tree.getroot()
                for child in root:
                    if child.tag == 'headline':
                        if child.text:
                            headlines.append(child.text)
    
    print('Headlines extracted successfully!')
    print('Number of headlines extracted:', len(headlines))
    return headlines

def store_headlines(headlines):
    # Have each word in the headline seperate in a new line
    # Seperate each headline with a new line
    print('Storing headlines...')
    with open('headlines.txt', 'w') as file:
        for headline in headlines:
            words = headline.split()
            for word in words:
                file.write(word + '\n')
            file.write('\n')
    print('Headlines stored successfully!')

def main():
    headlines = extract_headlines()
    store_headlines(headlines)


main()