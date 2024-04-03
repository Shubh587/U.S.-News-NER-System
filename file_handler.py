# Traverse through the Reuter's dataset in rcv1 and extract the new's headlines from all of the XML files
# and store them in a text file.
import os
import xml.etree.ElementTree as ET

def extract_headlines():
    rootdir = 'rcv1'
    headlines = []
    i = 0
    for subdir, dirs, files in os.walk(rootdir):
        if subdir == 'rcv1\\19960820':
            for file in files:
                if file.endswith('.xml'):
                    tree = ET.parse(os.path.join(subdir, file))
                    root = tree.getroot()
                    for child in root:
                        if child.tag == 'headline':
                            headlines.append(child.text)
    
    print('Headlines extracted successfully!')
    print(headlines)

def main():
    extract_headlines()

main()