# Importing the necessary Python libraries
import cv2
import os
import uuid
import time



## FILEPATH INSTANTIATION
## ---------------------------------------------------------------------------------------------------------------------
# Setting the name of the base images directory
BASE_IMAGES_FILEPATH = os.path.join('..', 'images')

# Setting the filepaths for the respective training and testing image storage locations
ALL_IMAGES_FILEPATH = os.path.join(BASE_IMAGES_FILEPATH, 'all_images')

# Collecting the filepaths into an iterable array
IMAGE_FILEPATHS = [BASE_IMAGES_FILEPATH, ALL_IMAGES_FILEPATH]

# Looping over IMAGE_FILEPATHS to create the directories if they do not already exist
for image_path in IMAGE_FILEPATHS:
    if not os.path.exists(image_path):
        os.mkdir(image_path)


## IMAGE CAPTURE
## ---------------------------------------------------------------------------------------------------------------------
# Setting the labels of the image types we will be capturing
IMAGE_LABELS = ['rock', 'paper', 'scissors']

# Setting the number of training / testing images to capture
NUM_IMAGES = 10

# Starting capture for each respective label
for label in IMAGE_LABELS:

    # Starting the video capture from the webcam
    video_capture = cv2.VideoCapture(0)

    # Starting capture of training images
    print(f'Starting capture of images for "{label}" in 5 seconds...')
    time.sleep(5)
    for image_number in range(NUM_IMAGES):
        print(f'Collecting "{label}" image #{image_number + 1}...')

        # Getting the captured frame from the webcam
        ret, frame = video_capture.read()

        # Creating the appropriate name of the image with a unique identifier
        image_name = os.path.join(ALL_IMAGES_FILEPATH, f'{label}-{str(uuid.uuid1())}.jpg')

        # Writing out the image file
        cv2.imwrite(image_name, frame)

        # Displaying the captured image
        cv2.imshow('Image Capture', frame)

        # Waiting 3 seconds for the next captured image
        time.sleep(3)

        # Allowing the user to break out of the image capture by pressing the "Q" key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Ending the image capture script appropriately
video_capture.release()
cv2.destroyAllWindows()