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
    imageH, imageW, _ = frame.shape
    
    # draw button with text
    cv2.rectangle(frame,(50,100),(200,150),(0,255,0),3)
    cv2.putText(frame,"Button",(80,130),cv2.FONT_ITALIC,1,(0,255,0),1)
    
    # Draw the hand annotations on the image.
    if result.multi_hand_landmarks:
        
      # iterate on all detected hand landmarks
      for hand_landmarks in result.multi_hand_landmarks:
        
        # print('Hand_landmarks:', hand_landmarks)
        
        # index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        index_finger_tip = hand_landmarks.landmark[8]
        
        
        # draw finger tip using coordinates from Mediapipe normalized output
        x=int(index_finger_tip.x*imageW)
        y=int(index_finger_tip.y*imageH)
        cv2.circle(frame,(x,y),2,(0,255,0),2)
        
        # check finger tip in button area
        if(50<x<200 and 100<y<150):
            # fill button
            cv2.rectangle(frame,(50,100),(200,150),(0,255,0),-1)
            #show response text
            cv2.putText(frame,"Button pressed",(50,50),cv2.FONT_ITALIC,1,(255,0,0),2)        
    cv2.imshow("Press button using Hand Gasture",frame)
    
    if cv2.waitKey(10) == 27:
      break