# Importing the required first party Python libraries
import os
import glob
from xml.etree import ElementTree

# Importing the required third party Python libraries
import pandas as pd



## FILEPATH & VARIABLE INSTANTIATION
## ---------------------------------------------------------------------------------------------------------------------
# Setting the filepaths where the XML files currently reside
XML_FILEPATHS = ['../images/training', '../images/validation']



## CONVERTING XML ANNOTATIONS TO CSV
## ---------------------------------------------------------------------------------------------------------------------
# Iterating through each of the respective XML filepath directories
for directory in XML_FILEPATHS:

    # Instantiating a list that will hold all the converted XML annotations
    xml_annotations = []

    # Iterating through each XML file in the respective filepath
    for xml_file in glob.glob(directory + '/*.xml'):

        # Instantiating an XML ElementTree
        xml_tree = ElementTree.parse(xml_file)

        # Getting the root from the XML ElementTree
        xml_root = xml_tree.getroot()

        # Getting the filename from the XML file
        filename = xml_root.find('filename').text

        # Getting the width and height of the original image
        width = int(xml_root.find('size')[0].text)
        height = int(xml_root.find('size')[1].text)

        # Getting the label type and bounding box coordinates
        for subelement in xml_root.findall('object'):
            object_class = subelement.find('name').text
            xmin = int(subelement[4][0].text)
            ymin = int(subelement[4][1].text)
            xmax = int(subelement[4][2].text)
            ymax = int(subelement[4][3].text)

        # Assembling the elements as a new entry to the collective list of XML-converted annotations
        new_entry = [filename, width, height, object_class, xmin, ymin, xmax, ymax]

        # Appending the new entry to the full list of XML-converted annotations
        xml_annotations.append(new_entry)