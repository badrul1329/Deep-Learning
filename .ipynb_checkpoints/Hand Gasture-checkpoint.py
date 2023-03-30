# MediaPipe is a powerful open-source framework developed by Google
# This model provides hand geometry solutions enabling the detection of 21 3D landmarks on human hands. Each landmark comprises three axes: the x, y, and z coordinates. These coordinates are normalized to values ranging between 0.0 and 1.0. last one,The depth how close the landmark is to the camera represents by the coordinate z.

# Import Libraries
import cv2
import mediapipe as mp

# VideoCapture - 0 for default cam, 1 for extensible
webcam = cv2.VideoCapture(0)

# drawing the hand landmarks on image
mp_drawing = mp.solutions.drawing_utils
# add styles onto the face
mp_drawing_styles = mp.solutions.drawing_styles

# main model
mp_hand = mp.solutions.hands

# Drawing the hand annotations on the image with several configuration
with mp_hand.Hands(
    # static_image_mode=True,
    max_num_hands=4,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5) as hands:
    
  while webcam.isOpened():
    # capture frame by frame
    control,frame = webcam.read()
    
    if control == False:
      break;
    
    # Converting the from BGR to RGB
    image_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # process image in RGB
    result = hands.process(image_rgb)
    
    if result.multi_hand_landmarks:
      for hand_landmarks in result.multi_hand_landmarks:
        # print('Hand_landmarks:', hand_landmarks)
        
        # draw results with different drawing settings
        mp_drawing.draw_landmarks(image=frame,
                                  landmark_list=hand_landmarks,
                                  connections=mp_hand.HAND_CONNECTIONS,
                                  landmark_drawing_spec=mp_drawing_styles
                                  .get_default_hand_landmarks_style(),
                                  connection_drawing_spec=mp_drawing_styles
                                  .get_default_hand_connections_style())
        
    cv2.imshow("Hand Gasture",frame)
    if cv2.waitKey(10) == 27:
      break