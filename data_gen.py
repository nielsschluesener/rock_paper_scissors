import cv2
import os

cam = cv2.VideoCapture(0)

cv2.namedWindow('data_gen')

raw_path = 'data/raw/'

rock_path = raw_path + 'rock/'
paper_path = raw_path + 'paper/'
scissor_path = raw_path + 'scissor/'
empty_path = raw_path + 'empty/'


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

if os.path.exists(empty_path):
    empty_counter = len(os.listdir(empty_path)) + 1
elif not os.path.exists(empty_path):
    os.makedirs(empty_path)
    empty_counter = 1

while True:
    ret, frame = cam.read()
    if not ret:
        print('failed to grab frame')
        break
    cv2.imshow('_', frame)

    k = cv2.waitKey(1)
    if k%256 == 27: # ESC
        print('Escape hit, closing...')
        break
    elif k == ord('r'):
        img_name = 'rock_{}.jpg'.format(rock_counter)
        resized_frame = cv2.resize(frame, (224, 224)) 

        cv2.imwrite(os.path.join(rock_path, img_name), resized_frame)
        print('{} written!'.format(img_name))
        rock_counter += 1
    elif k == ord('p'):
        img_name = 'paper_{}.jpg'.format(paper_counter)
        resized_frame = cv2.resize(frame, (224, 224)) 

        cv2.imwrite(os.path.join(paper_path, img_name), resized_frame)
        print('{} written!'.format(img_name))
        paper_counter += 1
    elif k == ord('s'):
        img_name = 'scissor_{}.jpg'.format(scissor_counter)
        resized_frame = cv2.resize(frame, (224, 224)) 

        cv2.imwrite(os.path.join(scissor_path, img_name), resized_frame)
        print('{} written!'.format(img_name))
        scissor_counter += 1
    elif k == ord('e'):
        img_name = 'empty_{}.jpg'.format(empty_counter)
        resized_frame = cv2.resize(frame, (224, 224)) 

        cv2.imwrite(os.path.join(empty_path, img_name), resized_frame)
        print('{} written!'.format(img_name))
        empty_counter += 1

cam.release()

cv2.destroyAllWindows()