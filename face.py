#시작 전 필수적으로 cmake 라이브러리 설치!
#시작 전 필수적으로 dlib 설치!
#시작 전 필수적으로 face_recognition 라이브러리 설치!

import face_recognition #face_recognition 모듈 가져오기
import cv2 #face_recognition
import numpy as np

#웹캠에서 영상 가져오기
video_capture = cv2.VideoCapture(0)

# 사진을 가져와 인식 학습하기
sowon_image = face_recognition.load_image_file("sowon.jpg")
sowon_face_encoding = face_recognition.face_encodings(sowon_image)[0]

# 인식할 얼굴
known_face_encodings = [
    sowon_face_encoding,
]
known_face_names = [
    "Kim Sowon"
]

while True:
    # 비디오의 프레임 잡기
    ret, frame = video_capture.read()

    # OpenCV에서 쓰는 BGR color를 face_recognition에서 사용하는 RGB color로 변환
    rgb_frame = frame[:, :, ::-1]

    # face_location 함수로 얼굴의 위치를 알아내 이미지 crop
    face_locations = face_recognition.face_locations(rgb_frame)
    # face_encodings 함수로 crop된 이미지를 인코딩하여 저장
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # 저장된 사진과 비디오로 들어오는 얼굴 비교
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        # face_distance 함수를 통해 인코딩된 데이터가 얼마나 유사한지 구함
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # 얼굴은 네모박스로 표시하기
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # 이름(라벨) 표시하기 
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # 결과 보여주기
    cv2.imshow('WebCam', frame)

    # 키보드 'q'를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#open된 웹캠 장치 닫음
video_capture.release()
cv2.destroyAllWindows()