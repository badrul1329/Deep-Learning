# MediaPipe is a powerful open-source framework developed by Google
# This model provides face geometry solutions enabling the detection of 468 3D landmarks on human faces. Each landmark comprises three axes: the x, y, and z coordinates. These coordinates are normalized to values ranging between 0.0 and 1.0. The depth,how close the landmark is to the camera represents by the coordinate z.
# The Face Mesh model uses machine learning to infer the 3D surface geometry on human faces. Utilizing the facial surface geometry has helped apply facial effects in AR applications


# Import Libraries
import cv2
import mediapipe as mp

# 0 for default cam, 1 for extensible
webcam = cv2.VideoCapture(0)

# drawing the facial landmarks on image
mp_drawing = mp.solutions.drawing_utils
# add styles onto the face
mp_drawing_styles = mp.solutions.drawing_styles

# main model
# MediaPipe FaceMesh is focused on 3D face tracking and head pose estimation
mp_face = mp.solutions.face_mesh

# adjust the thickness and circle radius
drawing_spec = mp_drawing.DrawingSpec(thickness=2, circle_radius=2)

# Drawing the face mesh annotations on the image
with mp_face.FaceMesh(
    # static_image_mode=True,
    refine_landmarks=True,
    max_num_faces=3,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5
) as face_mesh:
  while webcam.isOpened():
    # capture frame by frame
    control,frame = webcam.read()
    if control == False:
      break;
    # Converting the from BGR to RGB
    image_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    result = face_mesh.process(image_rgb)
    if result.multi_face_landmarks:
      for face_landmarks in result.multi_face_landmarks:
        # print('facial_landmarks:', face_landmarks)
        mp_drawing.draw_landmarks(image=frame,
                                  landmark_list=face_landmarks,
                                  connections=mp_face.FACEMESH_TESSELATION, 
                                  # landmark_drawing_spec=None,
                                  connection_drawing_spec=mp_drawing_styles
        # applies the face mesh’s style
                                  .get_default_face_mesh_tesselation_style()
                                 )
        
        mp_drawing.draw_landmarks(image=frame,
                                  landmark_list=face_landmarks,
                                  connections=mp_face.FACEMESH_CONTOURS,
                                  # landmark_drawing_spec=None,
                                  connection_drawing_spec=mp_drawing_styles
                                  .get_default_face_mesh_contours_style()
                                 )
        
        mp_drawing.draw_landmarks(image=frame,
                                  landmark_list=face_landmarks,
                                  connections=mp_face.FACEMESH_IRISES, 
                                  landmark_drawing_spec=None,
                                  connection_drawing_spec=mp_drawing_styles
                                  .get_default_face_mesh_iris_connections_style()
                                 )
    cv2.imshow("Face Gasture",frame)
    # Enter key 'esc' to break the loop
    if cv2.waitKey(10) == 27:
      break