import cv2



def get_frame():
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            # frame = cv2.flip(frame, 1)

            # write the flipped frame
            out.write(frame)

            cv2.imshow('this is the frame', frame)
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
            if cv2.waitKey(1) & 0xFF == ord('j'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
get_frame()