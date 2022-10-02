# Importing the necessary Python libraries
import os
import random
import shutil



## HELPER FUNCTIONS
## ---------------------------------------------------------------------------------------------------------------------
def get_split_counts(rps_label, jpg_filenames):
    '''
    Getting the 80-20 split counts for each respective label

    Inputs:
        - rps_label (str): The name of the label correlated to the jpg_filenames list
        - jpg_filenames (list): A list of the respective jpg filenames per the corelated label
    Returns:
        - num_training_images (int): The number of training images needed for this respective label
        - num_validation_images (int): The number of validation images needed for this respective label
    '''
    # Determining how many images to separate based on an 80-20 split for each label
    num_training_images = round(len(jpg_filenames) * .8)
    num_validation_images = len(jpg_filenames) - num_training_images

    # Printing the number of images correlated to each label and dataset
    print(f'Total number of images with the {rps_label} label: {len(jpg_filenames)}')
    print(f'Number of {rps_label} training images: {num_training_images}')
    print(f'Number of {rps_label} validation images: {num_validation_images}')

    return num_training_images, num_validation_images


## SCRIPT INITIATION
## ---------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    # Instantiating a list containing the three respective labels
    rps_labels = ['rock', 'paper', 'scissors']

    # Getting a list of all the filenames in the 'all_images' directory
    all_filenames = os.listdir('../images/all_images/')

    # Instantiating a dictionary to hold all lists
    rps_dict = {
        'rock': {
            'jpg_filenames': [],
            'jpg_training_filenames': [],
            'jpg_validation_filenames': [],
            'xml_filenames': [],
            'xml_training_filenames': [],
            'xml_validation_filenames': []
        },
        'paper': {
            'jpg_filenames': [],
            'jpg_training_filenames': [],
            'jpg_validation_filenames': [],
            'xml_filenames': [],
            'xml_training_filenames': [],
            'xml_validation_filenames': []
        },
        'scissors': {
            'jpg_filenames': [],
            'jpg_training_filenames': [],
            'jpg_validation_filenames': [],
            'xml_filenames': [],
            'xml_training_filenames': [],
            'xml_validation_filenames': []
        },
    }

    # Splitting the filenames by respective label
    for filename in all_filenames:

        # Getting the label prefix of the filename
        filename_prefix = filename.split('-')[0]

        # Getting the file type suffix of the filename
        filename_suffix = filename.split('.')[1]

        # Sorting the filenames into their respective groups
        if filename_prefix == 'rock' and filename_suffix == 'jpg':
            rps_dict['rock']['jpg_filenames'].append(filename)
        elif filename_prefix == 'rock' and filename_suffix == 'xml':
            rps_dict['rock']['xml_filenames'].append(filename)
        elif filename_prefix == 'paper' and filename_suffix == 'jpg':
            rps_dict['paper']['jpg_filenames'].append(filename)
        elif filename_prefix == 'paper' and filename_suffix == 'xml':
            rps_dict['paper']['xml_filenames'].append(filename)
        elif filename_prefix == 'scissors' and filename_suffix == 'jpg':
            rps_dict['scissors']['jpg_filenames'].append(filename)
        elif filename_prefix == 'scissors' and filename_suffix == 'xml':
            rps_dict['scissors']['xml_filenames'].append(filename)

    # Instantiating containers to hold all training and validation filenames
    training_filenames, validation_filenames = [], []

    # Iterating through each of the three labels
    for label in rps_labels:

        # Getting the number of training and validation images
        num_training_images, num_validation_images = get_split_counts(label, rps_dict[label]['jpg_filenames'])
        rps_dict[label]['num_training_images'] = num_training_images
        rps_dict[label]['num_valididation_images'] = num_validation_images

        # Shuffling the jpg_filenames
        random.shuffle(rps_dict[label]['jpg_filenames'])

        # Setting the jpg training and validation filenames with numbers derived above
        rps_dict[label]['jpg_training_filenames'] = rps_dict[label]['jpg_filenames'][:num_training_images]
        rps_dict[label]['jpg_validation_filenames'] = rps_dict[label]['jpg_filenames'][num_training_images:]

        # Getting the correlative XML filenames per each respective JPG training / validation set
        for xml_filename in rps_dict[label]['xml_filenames']:

            # Getting the prefix for the XML filename
            xml_prefix = xml_filename.split('.')[0]

            # Crafting a dummy JPG filename to check against the respective JPG training / validation sets
            jpg_dummy = f'{xml_prefix}.jpg'

            # Sorting the XML files into the respective training / validation sets
            if jpg_dummy in rps_dict[label]['jpg_training_filenames']:
                rps_dict[label]['xml_training_filenames'].append(xml_filename)
            elif jpg_dummy in rps_dict[label]['jpg_validation_filenames']:
                rps_dict[label]['xml_validation_filenames'].append(xml_filename)

        # Appending to the final training and validation filenames
        training_filenames += rps_dict[label]['jpg_training_filenames'] + rps_dict[label]['xml_training_filenames']
        validation_filenames += rps_dict[label]['jpg_validation_filenames'] + rps_dict[label]['xml_validation_filenames']

    # Creating the new directories to hold the training and validation files
    if not os.path.exists('../images/training'):
        os.mkdir('../images/training')
    if not os.path.exists('../images/validation'):
        os.mkdir('../images/validation')

    # Copying all the training files from the 'all_images' directory into the new 'training' directory
    for filename in training_filenames:

        # Defining source and destination filepaths
        source_filepath = f'../images/all_images/{filename}'
        destination_filepath = f'../images/training/{filename}'

        # Copying the files over to the new directory
        shutil.copy(source_filepath, destination_filepath)

    # Copying all the training files from the 'all_images' directory into the new 'validation' directory
    for filename in validation_filenames:

        # Defining source and destination filepaths
        source_filepath = f'../images/all_images/{filename}'
        destination_filepath = f'../images/validation/{filename}'

        # Copying the files over to the new directory
        shutil.copy(source_filepath, destination_filepath)