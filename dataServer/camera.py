import cv2

def cam():
    camera = cv2.VideoCapture(0)
    while camera.isOpend():
        success, frame = camera.read()
        if success:
            cv2.imshow("camera",frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    camera.release()
    cv2.destroyAllWindows()