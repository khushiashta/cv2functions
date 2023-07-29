import cv2

# read the input image
img = cv2.imread('image.jpeg')

# convert to grayscale of each frames
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# read the haarcascade to detect the faces in an image
face_cascade = cv2.CascadeClassifier('/cutting image/haarcascade/haarcascade_frontalface_alt.xml')

# detects faces in the input image
faces = face_cascade.detectMultiScale(gray, 1.3, 4)
print('Number of detected faces:', len(faces))

# loop over all detected faces
if len(faces) > 0:
    for i, (x, y, w, h) in enumerate(faces):
        face = img[y:y + h, x:x + w]
        cv2.imshow("Cropped Face", face)
        cv2.imwrite(f'face{i}.jpg', face)
        print(f"face{i}.jpg is saved")



