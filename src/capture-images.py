# Importing the necessary Python libraries
import cv2
import uuid
import os
import time

## FILEPATH INSTANTIATION
## ---------------------------------------------------------------------------------------------------------------------
# Setting the name of the base images directory
BASE_IMAGES_FILEPATH = os.path.join('..', 'images')

# Setting the filepaths for the respective training and testing image storage locations
TRAINING_IMAGES_FILEPATH = os.path.join(BASE_IMAGES_FILEPATH, 'train')
TESTING_IMAGES_FILEPATH = os.path.join(BASE_IMAGES_FILEPATH, 'test')

# Collecting the filepaths into an iterable array
IMAGE_FILEPATHS = [BASE_IMAGES_FILEPATH, TRAINING_IMAGES_FILEPATH, TESTING_IMAGES_FILEPATH]

# Creating the image path if it does not already exist
for image_path in IMAGE_FILEPATHS:
    if not os.path.exists(image_path):
        os.mkdir(image_path)



## IMAGE CAPTURE
## ---------------------------------------------------------------------------------------------------------------------
# Setting the labels of the image types we will be capturing
IMAGE_LABELS = ['rock', 'paper', 'scissors']

# Setting number of training / testing images to capture
NUM_TRAIN_IMAGES = 8
NUM_TEST_IMAGES = 2

# Starting capture for each respective label
for label in IMAGE_LABELS:

    # Starting the video capture from the webcam
    video_capture = cv2.VideoCapture(0)

    # Starting capture of training images
    print(f'Starting capture of training images for "{label}" in 5 seconds...')
    time.sleep(5)
    for image_number in range(NUM_TRAIN_IMAGES):
        print(f'Collecting "{label}" training image #{image_number + 1}...')

        # Getting captured frame from the webcam
        ret, frame = video_capture.read()

        # Creating the appropriate name of the image with a unique identifier
        image_name = os.path.join(TRAINING_IMAGES_FILEPATH, f'{label}.{str(uuid.uuid1())}.jpg')

        # Writing out the image to file
        cv2.imwrite(image_name, frame)

        # Displaying the captured image
        cv2.imshow('Image Capture', frame)

        # Waiting 2 seconds for next captured image
        time.sleep(2)

        # Allowing user to break out of image capture by pressing the "Q" key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Starting capture of testing images
    print(f'Starting capture of testing images for "{label}" in 5 seconds...')
    time.sleep(5)
    for image_number in range(NUM_TEST_IMAGES):
        print(f'Collecting "{label}" testing image #{image_number + 1}...')

        # Getting captured frame from the webcam
        ret, frame = video_capture.read()

        # Creating the appropriate name of the image with a unique identifier
        image_name = os.path.join(TESTING_IMAGES_FILEPATH, f'{label}.{str(uuid.uuid1())}.jpg')

        # Writing out the image to file
        cv2.imwrite(image_name, frame)

        # Displaying the captured image
        cv2.imshow('Image Capture', frame)

        # Waiting 2 seconds for next captured image
        time.sleep(2)

        # Allowing user to break out of image capture by pressing the "Q" key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# Ending the image capture script appropriately
video_capture.release()
cv2.destroyAllWindows()