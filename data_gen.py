import cv2
import os

#Configuration of paths
raw_path = 'data/raw/'
rock_path = raw_path + 'rock/'
paper_path = raw_path + 'paper/'
scissor_path = raw_path + 'scissor/'

#Create counters for img-names and folders if they dont exist yet.

if os.path.exists(rock_path):
    rock_counter = len(os.listdir(rock_path)) + 1
elif not os.path.exists(rock_path):
    os.makedirs(rock_path)
    rock_counter = 1

if os.path.exists(paper_path):
    paper_counter = len(os.listdir(paper_path)) + 1
elif not os.path.exists(paper_path):
    os.makedirs(paper_path)
    paper_counter = 1

if os.path.exists(scissor_path):
    scissor_counter = len(os.listdir(scissor_path)) + 1
elif not os.path.exists(scissor_path):
    os.makedirs(scissor_path)
    scissor_counter = 1

#Adress Webcam and create a window that shows a livestream of input-frames
cam = cv2.VideoCapture(0)
cv2.namedWindow('data_gen')

while True:
    ret, frame = cam.read()
    if not ret:
        print('failed to grab frame')
        break
    cv2.imshow('_', frame)

    #Enable user to take a picture for a certain class by pressing a letter assigned to a class, e.g. "r" for "rock" on his keyboard.
    #The picture gets saved in a designated subfolder.

    k = cv2.waitKey(1)
    if k%256 == 27: # ESC
        print('Escape hit, closing...')
        break
    elif k == ord('r'):
        img_name = 'rock_{}.jpg'.format(rock_counter)
        cv2.imwrite(os.path.join(rock_path, img_name), frame)
        print('{} written!'.format(img_name))
        rock_counter += 1
    elif k == ord('p'):
        img_name = 'paper_{}.jpg'.format(paper_counter)
        cv2.imwrite(os.path.join(paper_path, img_name), frame)
        print('{} written!'.format(img_name))
        paper_counter += 1
    elif k == ord('s'):
        img_name = 'scissor_{}.jpg'.format(scissor_counter)
        cv2.imwrite(os.path.join(scissor_path, img_name), frame)
        print('{} written!'.format(img_name))
        scissor_counter += 1

#If "ESC" gets pressed, the app stops.
cam.release()
cv2.destroyAllWindows()

