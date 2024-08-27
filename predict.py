from ultralytics import YOLO
import cv2


cap = cv2.VideoCapture(0)

while (True):
    ret,frame = cap.read()
    cv2.imwrite("capture.png",frame)
    break


image_path = "./capture.png"
img = cv2.imread(image_path)

model = YOLO("./trainedWeights/last.pt")
result = model(img)[0]

bestPrediction = 0
bestMask = result.masks.data[0]
mask = bestMask.numpy()*255

cv2.imwrite(f"mask.png",mask)


