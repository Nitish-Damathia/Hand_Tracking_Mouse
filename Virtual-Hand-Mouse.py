#Use your index finger to move the cursor and join your middle finger with index finger for click

import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_w,screen_h =pyautogui.size()
index_y = 0
while True:
    _,frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_h,frame_w,_ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_w)
                y = int(landmark.y*frame_h)
                print(x,y)
                if id == 8:
                    cv2.circle(frame,(x,y),10,(0,255,255))
                    index_x = screen_w/frame_w*x
                    index_y = screen_h/frame_h*y
                    pyautogui.moveTo(index_x,index_y)
                if id == 12:
                    cv2.circle(frame,(x,y),10,(0,255,255))
                    thumb_x = screen_w/frame_w*x
                    thumb_y = screen_h/frame_h*y
                    print(abs(thumb_y-index_y))
                    if abs(thumb_y-index_y)<100:
                        pyautogui.click()
                        pyautogui.sleep(1)





    cv2.imshow('Virtual Mouse',frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
