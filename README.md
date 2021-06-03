# Face-recognition
## Implementing one of face recognition algorithms
PC 카메라 영상에 나타나는 사람을 인식하여 정보를 표시한다.   

### 알고리즘
얼굴을 인식하기 위해서는 다음과 같은 세 단계를 거칩니다.   

1. 이미지에서 얼굴이 있는 영역을 알아낸다. (face location)   
2. 얼굴 영역에서 눈, 코, 입 등 68개의 주요 좌표를 추출한다. (facial landmarks)   
3. 68개의 좌표를 128개의 숫자로 변환한다. (face encoding)   
   
파이썬 패키지 dlib에는 이 과정이 face_recognition 패키지의 face_location()과 face_encodings() 함수로 구현되어 있습니다.    
설명 참고 링크 : https://ukayzm.github.io/unknown-face-classifier/   

#### 코드
Face_recognition 패키지
https://github.com/ageitgey/face_recognition
